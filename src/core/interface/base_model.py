# https://blog.hwahae.co.kr/all/tech/tech-tech/4108
# https://wikidocs.net/6667

from django.db import models
from django.db.models import ExpressionWrapper
from django.db.models import F
from django.utils import timezone


class BaseModelManager(models.Manager):
    def get_active_count(self):
        """삭제 되지 않은 개수 구하기"""
        return self.get_queryset().filter_active().count()


class BaseModelQuerySet(models.QuerySet):
    def filter_active(self):
        return self.filter(deleted_at__isnull=True)

    def annotate_days_since_creation(self):
        """생성 된지 얼마나 지났는지 timedelta 구하기"""
        return self.annotate(
            days_since_creation=ExpressionWrapper(timezone.now() - F('created_at'), output_field=models.DurationField())
        )


class BaseModel(models.Model):
    objects = BaseModelManager.from_queryset(BaseModelQuerySet)()

    created_at = models.DateTimeField('생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시간', auto_now=True)
    deleted_at = models.DateTimeField('삭제 시간', null=True, blank=True)

    class Meta:
        abstract = True
        default_manager_name = "objects"
        ordering = ['-id']

    def delete(self):
        """Soft-Delete 구현"""
        self.deleted_at = timezone.now()
        self.save()
        return self

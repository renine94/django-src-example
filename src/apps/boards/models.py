from django.db import models

from src.core.interface.base_model import BaseModel

# Create your models here.


class Article(BaseModel):
    title = models.CharField('제목', max_length=120)
    content = models.TextField('내용')

    class Meta:
        verbose_name = '아티클'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.title

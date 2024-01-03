from django.contrib import admin

from src.apps.boards.models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    ordering = ['-id']

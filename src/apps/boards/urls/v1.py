from django.urls import path

from src.apps.boards.views import v1

urlpatterns = [
    path("board/", v1.index),
]

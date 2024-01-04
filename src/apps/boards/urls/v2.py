from django.urls import path

from src.apps.boards.views import v2

urlpatterns = [
    path("board/", v2.index),
]

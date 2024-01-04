from django.urls import path

from src.apps.accounts.views import v1

urlpatterns = [
    path("user/", v1.index),
]

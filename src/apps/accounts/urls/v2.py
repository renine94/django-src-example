from django.urls import path

from src.apps.accounts.views import v2

urlpatterns = [
    path("user/", v2.index),
]

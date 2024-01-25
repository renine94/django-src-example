from django.urls import path

from src.apps.accounts.views import v1

app_name = 'accounts'
urlpatterns = [
    path("user/", v1.index),
    path("test/<int:pk>/", v1.TestAPI.as_view(), name='test-api'),
]

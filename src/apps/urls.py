from django.urls import include
from django.urls import path

urlpatterns = [
    path("v1/", include('src.apps.accounts.urls.v1')),
    path("v1/", include('src.apps.boards.urls.v1')),
    path("v2/", include('src.apps.accounts.urls.v2')),
    path("v2/", include('src.apps.boards.urls.v2')),
]

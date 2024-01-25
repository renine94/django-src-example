from django.urls import path

from src.apps.accounts.views import v1 as view_v1

app_name = 'accounts'
urlpatterns = [
    # User
    path("users/", view_v1.index, name='user-list'),
    path("users/<int:pk>/", view_v1.index, name='user-detail'),

    # Test
    path("test/<int:pk>/", view_v1.TestAPI.as_view(), name='test-api'),
]

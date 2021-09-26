from django.urls import include, path
from .views import UserApi
urlpatterns = [
    path('users/register', UserApi.as_view()),
]
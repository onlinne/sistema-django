from django.urls import include, path
from .views import UserApi
urlpatterns = [
    path('users', UserApi.as_view()),
]
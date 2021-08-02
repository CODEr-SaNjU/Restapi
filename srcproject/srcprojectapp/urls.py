from django.urls import path
from .views import UserCreateApiView , UserLoginApiView



urlpatterns = [
    path('create_user/',UserCreateApiView.as_view(),name="registration_user"),
    path('login/',UserLoginApiView.as_view(),name='login_user'),
]

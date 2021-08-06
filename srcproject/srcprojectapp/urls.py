from django.urls import path,include
from rest_framework import views
from .views import UserCreateApiView , UserLoginApiView ,UserPasswordRestApiView ,lead_list,lead_detail,lead_create,lead_delete,lead_partial_update,lead_update





urlpatterns = [
    path('create_user/',UserCreateApiView.as_view(),name="registration_user"),
    path('login/',UserLoginApiView.as_view(),name='login_user'),
    path('rest_password/',UserPasswordRestApiView.as_view(),name='rest_password'),
    # path('email-verify/',VerifyEmail.as_view(),name='email-verify'),
    path('lead/list/',lead_list,name="lead_list"),
    path('lead/create/',lead_create,name='lead_create'),
    path('lead/update/<pk>/',lead_update,name='lead_update'),
    path('lead/partial_update/<pk>/',lead_partial_update,name="lead_partial_update"),
    path('lead/deatil/<pk>/',lead_detail,name='lead_detail'),
    path('lead/delete/<pk>/',lead_delete,name="lead_delete"),
]

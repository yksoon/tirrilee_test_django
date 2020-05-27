from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signup_check/', views.signup_check, name='signup_check'),
]
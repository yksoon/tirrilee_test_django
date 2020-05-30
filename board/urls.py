from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('result/', views.search_result, name='search_result'),
    path('community/', views.community, name='community'),
    path('community/add', views.community_add, name='community_add'),
]

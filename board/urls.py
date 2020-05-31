from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('result/', views.search_result, name='search_result'),
    path('community/', views.community, name='community'),
    path('community/add', views.community_add, name='community_add'),
    path('community/add/result', views.community_add_result, name='community_add_result'),
    path('mypage/', views.mypage, name='mypage'),
    path('logout/', views.logout, name='logout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

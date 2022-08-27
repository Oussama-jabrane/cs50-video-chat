from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='index'),
    path('room/', views.room, name='room'),
    path('get-token/', views.getToken, name='token'),
    path('create_member/', views.createMember, name='create-user'),
    path('get_member/', views.getMember, name='get-member'),
    path('delete_member/', views.deleteMember, name='get-member'),
]
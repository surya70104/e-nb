from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('add/', views.add_notice, name='add_notice'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

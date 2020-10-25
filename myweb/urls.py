from django.urls import path,include
from django.contrib.auth import views as aunt_views
from . import views



urlpatterns = [

    path('index', views.index, name='index'),
    path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('logout/', views.logout, name='logout'),


    path('stand/', views.stand, name='stand'),
    path('stand1/', views.stand1, name='stand1'),
    path('stand2/', views.stand2, name='stand2'),
    path('stand3/', views.stand3, name='stand3'),
    path('stand4/', views.stand4, name='stand4'),
    path('stone/', views.stone, name='stone'),
    path('stone1/', views.stone1, name='stone1'),
    path('stone2/', views.stone2, name='stone2'),
    path('stone3/', views.stone3, name='stone3'),
    path('stone4/', views.stone4, name='stone4'),
]

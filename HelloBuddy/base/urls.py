#this is for url for specific APPs
from django.urls import path,include 
from . import views

urlpatterns = [    
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('',views.home,name="home"), #require 3 para endpoint then we go to views.py and name a view to name for reference
    path('room/<str:pk>/',views.room,name="room"), #pk=primary key
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>/',views.deleteMessage,name="delete-message"),

    path('update-user/',views.updateUser,name="update-user"),

    path('topics/',views.topicsPage,name="topics"),
    
    path('activity/',views.activityPage,name="activity"),
]
 

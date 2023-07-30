from django.urls import path
from . import views

urlpatterns=[
    path('',views.getRoutes), #this path is empty string
    path('rooms/',views.getRooms),
    path('rooms/<str:pk>/',views.getRoom),

]
from django.contrib import admin
from django.urls import path, include
from TodoApp import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('task',views.task, name="task"),
    # path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]

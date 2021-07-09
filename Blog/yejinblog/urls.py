from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"), # main.html
    path('guest/', views.guest, name="guest"), #guest.html
    # path('word_count/', views.word_count, name="word_count"),
    path('login/', views.login, name="login"),

    path('project/',views.project, name="project"),
    path('<str:id>', views.detail, name="detail"),
    path('<str:id>', views.detail_projecting, name="detail_projecting"),
 
    path('study/', views.study, name="study"),
]
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
    path('create_project/',views.create, name="create"),
    path('new/',views.new,name="new"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('update/<str:id>', views.update, name="update"),


    path('<str:id>', views.detail_projecting, name="detail_projecting"),
    path('create_projecting/', views.create_projecting, name="create_projecting"),
    path('new_projecting/',views.new_projecting, name="new_projecting"),
    path('delete_projecting/<str:id>', views.delete_projecting, name="delete_projecting"),

    path('study/', views.study, name="study"),
]
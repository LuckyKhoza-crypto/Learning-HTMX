from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_form/', views.add_form, name="add_form"),
    path('edit_click/<int:pk>', views.edit_click, name="edit_click"),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete_todo'),
]

from django.urls import path, include
from . import views

app_name = 'itn'

urlpatterns = [
    path('', views.main, name='main'),
    path('forms/', views.forms, name='forms'),
    path('groups/', views.groups, name='groups'),
    path('uploads/', views.uploads, name='uploads'),
    path('post_form/', views.post, name='post_form'),
]

from django.urls import path
from . import views

app_name= 'accounts'

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('login_required/', views.login_required, name='login_required'),
]

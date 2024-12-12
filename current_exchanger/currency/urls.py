from django.urls import path
from . import views
app_name = 'currency'

urlpatterns = [
    path('currency/table/', views.table, name='table'),
    path('currency/changer/', views.changer, name='changer'),
    
    path('auth/login/', views.UserLogin, name='login'),
    path('auth/register/', views.UserRegister, name='register'),
    path('auth/logout/', views.UserLogout, name='logout'),
]
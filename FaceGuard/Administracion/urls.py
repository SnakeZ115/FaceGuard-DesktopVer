from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login/', views.login_process, name="login_process"),
    path('registros',views.registros, name="registros"),
]
from django.urls import path, include
from login import views

urlpatterns = [
    path('login', views.login_, name = 'login'),
    path('demo', views.demo, name = 'demo'),
    path('accounts', include('django.contrib.auth.urls')),
]
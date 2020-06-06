from django.urls import path, include
from login_page import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_, name = 'login'),
    path('logout/', views.logout_, name = 'logout'),
]

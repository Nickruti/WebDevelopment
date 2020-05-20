from django.urls import path, include
from add_sites import views

urlpatterns = [
    path('', views.add_sites, name = 'addsite'),
]
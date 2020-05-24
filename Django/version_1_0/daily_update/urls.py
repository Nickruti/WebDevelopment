from django.urls import path, include
from daily_update import views

urlpatterns = [
    path('', views.dailyUpdate, name = 'dailyUpdate'),
    path('table/', views.dailyUpdate_list, name = 'dailyUpdateTable'),
]
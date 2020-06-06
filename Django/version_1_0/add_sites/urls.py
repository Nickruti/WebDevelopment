from django.urls import path, include
from add_sites import views

urlpatterns = [
    path('', views.add_sites, name = 'addsite'),
]
#login_required(TemplateView.as_view(template_name="login.html"))
from django.contrib import admin
from login.models import Login
# Register your models here.
 
class LoginAdmin(admin.ModelAdmin):
    pass

admin.site.register(Login, LoginAdmin)

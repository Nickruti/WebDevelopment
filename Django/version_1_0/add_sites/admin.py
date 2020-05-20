from django.contrib import admin
from add_sites.models import AddSites
# Register your models here.
 
class AddSiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(AddSites, AddSiteAdmin)

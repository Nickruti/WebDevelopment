from django.contrib import admin
from daily_update.models import DailyUpdate, Materials
# Register your models here.
 
class DailyUpdateAdmin(admin.ModelAdmin):
    pass

class MaterialsAdmin(admin.ModelAdmin):
    pass

admin.site.register(DailyUpdate, DailyUpdateAdmin)
admin.site.register(Materials, MaterialsAdmin)
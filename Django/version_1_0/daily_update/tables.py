import django_tables2 as tables
from .models import DailyUpdate

class DailyUpdateTable(tables.Table):
    class Meta:
        model = DailyUpdate
        template_name = "django_tables2/bootstrap.html"
        fields = ("date", "total_workers", "male_coolie", "female_coolie", "mason", "centric_fitter", "materials_purchased", "material_details"  )

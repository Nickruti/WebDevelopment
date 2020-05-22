from django.db import models
from add_sites.models import AddSites

# Create your models here.
class Materials(models.Model):
    material_name = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.material_name

class DailyUpdate(models.Model):
    siteid = models.ForeignKey(AddSites, on_delete=models.CASCADE, null=True)
    day = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    total_workers = models.IntegerField(blank=True)
    male_coolie = models.IntegerField(blank=False)
    female_coolie = models.IntegerField(blank=True)
    mason = models.IntegerField(blank=True)
    centric_fitter = models.IntegerField(blank=True)
    materials_purchased = models.ForeignKey(Materials, models.SET_NULL, blank=True, null=True)
    material_details = models.TextField(null=True)
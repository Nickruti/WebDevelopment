from django.db import models

# Create your models here.
class AddSites(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=False) 

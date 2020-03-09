from django.db import models

# Create your models here.
class Reports(models.Model):
    u_name=models.CharField(max_length=64)
    mob_nu=models.IntegerField()
    address=models.CharField(max_length=128)
    u_image=models.ImageField(upload_to='images/')
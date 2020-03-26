from django.db import models

# Create your models here.
class Reports(models.Model):
    title=models.CharField(max_length=64)
    u_image=models.ImageField(upload_to='images/')
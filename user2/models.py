from django.db import models

# Create your models here.
class Checking(models.Model):
    u2_image=models.ImageField(upload_to='test_img/')
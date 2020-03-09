from django.contrib import admin
from user2.models import Checking
# Register your models here.
class User2_Admin(admin.ModelAdmin):
    list_display=['id','u2_image']

admin.site.register(Checking,User2_Admin)
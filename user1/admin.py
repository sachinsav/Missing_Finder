from django.contrib import admin
from .models import Reports
# Register your models here.
class ReportsAdmin(admin.ModelAdmin):
    list_display=['id','title','u_image']

admin.site.register(Reports,ReportsAdmin)
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user1.models import Reports
from user1.serializers import ReportSerializers
from user2.views import User2

# Create your views here.
class ReportOperation(ModelViewSet):
    queryset=Reports.objects.all()
    serializer_class=ReportSerializers
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user2.models import Checking
from user2.serializers import User2Serializer
# Create your views here.
class User2(ModelViewSet):
    queryset=Checking.objects.all()
    serializer_class=User2Serializer
   
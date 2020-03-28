from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user2.models import Checking
from user2.serializers import User2Serializer
#from user2.testing import Test
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import user2.face_rec as fr
from django.http import HttpResponse

# Create your views here.
class User2(APIView):
    
    def get(self,request):
        check=Checking.objects.all()
        serializer = User2Serializer(check,many=True)
        return Response(serializer.data)
    
    def post(self, requests):
        serializer = User2Serializer(data=requests.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User2Detail(APIView):
    def get_object(self,id):
        try:
            return Checking.objects.get(id=id)
        except Checking.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        check=self.get_object(id)
        serializer=User2Serializer(check)
        return Response(serializer.data)
    def put(self,request,id):
        check=self.get_object(id)
        serializer = User2Serializer(check,data=request.data)
        
        if(serializer.is_valid()):
            serializer.save()
            x="1"
            x=fr.run()
            print(x)
            return Response(x)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        check = self.get_object(id)
        check.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
    # def index(request):
    #     #Test.pri()
    #     x=fr.run()
    #     print(x)
    #     #return HttpResponse('hii')
    #     return HttpResponse(x)

# User2().index()
        

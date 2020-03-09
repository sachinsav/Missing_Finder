from user2.models import Checking
from rest_framework.serializers import ModelSerializer
class User2Serializer(ModelSerializer):
    class Meta:
        model=Checking
        fields='__all__'
from user1.models import Reports
from rest_framework.serializers import ModelSerializer
class ReportSerializers(ModelSerializer):
    class Meta:
        model=Reports
        fields='__all__'
from rest_framework.serializers import BaseSerializer,ModelSerializer
from student.models import Students

class studentserialization(ModelSerializer):
    class Meta:
        model= Students
        fields='__all__'
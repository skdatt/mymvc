from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from student.models import Students
from student.serializer import studentserialization
from rest_framework.permissions import AllowAny,IsAdminUser


class studentoperation(ModelViewSet):
    permission_classes = (AllowAny,)  #make it public
    queryset = Students.objects.all()
    serializer_class = studentserialization
    def get_permissions(self):
        if self.action in ('destroy', ): #Method to be secured
            self.permission_classes = [IsAdminUser,]
        return super(self.__class__, self).get_permissions()
# Create your views here.

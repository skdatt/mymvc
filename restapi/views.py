from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet,GenericViewSet,ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin
from restapi.models import Book
from restapi.serializer import Bookserialization
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly

class Bookopretions(ModelViewSet): #all opretation create,put,post,delete,get etc
      permission_classes = (AllowAny,)
      queryset = Book.objects.all()
      serializer_class = Bookserialization


'''commented
class mymixin(CreateModelMixin,UpdateModelMixin,GenericViewSet): #
    pass

class Bookopretions(mymixin):#custom view set only create,update
      queryset = Book.objects.all()
      serializer_class = Bookserialization

'''

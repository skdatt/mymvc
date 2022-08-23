from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from restapi.models import Book
#from models import Book

class Bookserialization(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'      #if all fields in model to be serialized
        #fields= ('id','Name','Price')  #if only perticular fields in model to be serialized
        #exclude=('id','Name')    #except these fields all other fields in model to be serialized



#Include classes that take models or objects and convert to JSON object and then we can return it

from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializers(ModelSerializer):
    class Meta: #we have to spicify 2 fields at minimum
        model= Room
        fields='__all__'
        #This will return room model into json object
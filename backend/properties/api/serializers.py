# In Django Rest Framework (DRF), serializers are used to convert Django models into JSON format, which can then be used to send data to a client or API. 
from rest_framework import serializers
from .models import House, Rooms, House_Rooms

# The HouseSerializer is a serializer class that defines the fields that should be serialized for a House model, as well as any additional logic that should be applied during serialization.
class HouseSerializer(serializers.ModelSerializer):

    # rooms field is a SerializerMethodField, which is a special type of field that allows you to define a method on the serializer to return a value for the field. 
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = ['id', 'name', 'rooms']

    # get_room_names method is the function that is called to return the value for the room_names field.
    def get_rooms(self, house):
        # Retrieve the related rooms using the house_rooms field
        rooms = house.house_rooms_set.all()
        return [object.room.name for object in rooms]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['__all__']
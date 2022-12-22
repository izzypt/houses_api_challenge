from .models import House, Rooms , House_Rooms
from .serializers import HouseSerializer, RoomSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def getHouses(request, num_room):
	if num_room != "all":
		# Get the houses and count the number of bedrooms for each house, annotating that number to each object
		houses = House.objects.annotate(num_bedrooms=Count('house_rooms', filter=Q(house_rooms__room__name='bedroom')))
		# Filter the houses to include only those that have the specified number of bedrooms
		houses = houses.filter(num_bedrooms=num_room)
	else:
		houses = House.objects.all()
	serializer = HouseSerializer(houses, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def deleteHouse(request):
    # Get the house ID from the request
    house_id = request.data.get('house_id')
    print("The house id we received: ", house_id)
    # Fetch Object
    house = get_object_or_404(House, pk=house_id)

    # Delete it
    house.delete()
    return Response(status=status.HTTP_202_ACCEPTED, data={"Message": "Success"})

@api_view(['POST'])
def addHouse(request):
    # Get the data from the request
    house_name = request.data.get('house_name')
    room_names = request.data.get('room_names')

    # Create a new House object
    house = House.objects.create(name=house_name)

    # Create a new Rooms object for each room name
    rooms = []
    for room_name in room_names:
        room = Rooms.objects.create(name=room_name)
        rooms.append(room)

    # Create a House_Rooms object for each room and associate it with the house
    for room in rooms:
        House_Rooms.objects.create(house=house, room=room)

    return Response(status=status.HTTP_202_ACCEPTED, data={"Message": "Success"})

@api_view(['POST'])
def updateHouse(request):
    # Get the data from the request
    house_id = request.data.get('house_id')
    house_name = request.data.get('house_name')
    room_names = request.data.get('room_names')

    # Get the House object to be updated
    house = House.objects.get(pk=house_id)

    # Update the house name
    house.name = house_name
    house.save()

    # Delete the existing House_Rooms objects for this house
    House_Rooms.objects.filter(house=house).delete()

    # Create a new Rooms object for each room name
    rooms = []
    for room_name in room_names:
        room = Rooms.objects.create(name=room_name)
        rooms.append(room)

    # Create a House_Rooms object for each room and associate it with the house
    for room in rooms:
        House_Rooms.objects.create(house=house, room=room)

    return Response(status=status.HTTP_202_ACCEPTED, data={"Message": "Success"})

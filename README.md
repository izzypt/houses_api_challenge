# Uniplaces exercise

Solving the first exercise sent from Uniplaces for Jr. Full Stack position

[Section 1 - The Problem](#TheProblem)

[Section2 - Solution Process](#Solutionprocess)



# The problem <a id="TheProblem"></a>

  Properties are very special objects of our domain. Properties can have multiple Units.
  Assume that properties have a unique name. Each property have an array of units, and
  each unit can have the following values:
  
  - kitchen
  - bathroom
  - bedroom
  - living-room

## Objective

1. Create a REST endpoint to add a new Property in one POST request:

 ###
    {
      "name":"Yellow apartment",
      "units":["kitchen","bathroom","bedroom"]
    }
    POST /properties
    
 2. Create an endpoint to delete a property.
 
 ###
    {
      "name":"Yellow apartment"
    }
    DELETE /properties
    
 3. Create an endpoint to fetch all Properties. The results should be sorted by the property name.
 
 ###
    GET /properties
    Response:
    {
      properties: [
        {
          "name":"Yellow apartment",
          "units":["kitchen","bathroom","bedroom"]
        },
        {
          "name":"Red apartment",
          "units":["kitchen","bathroom","bedroom","bedroom","living-room"]
        }
       ]
    }
    
 4. Create a frontend to list all properties using the API built on point 3.
   
### Optional

5. Add to the frontend the possibility to add new properties;

6. Add to the frontend the possibility to delete each property;

7. Add on the GET properties backend endpoint the possibility to filter by the
number of bedrooms. On the example showed on point 3, if we wanted to get all
properties with 2 bedrooms should return:

###
    {
      properties: 
      [
          {
            "name":"Red apartment",
            "units":["kitchen","bathroom","bedroom","bedroom","living-room"]
          }
      ]
    } 
    
# Solution process <a id="Solutionprocess"></a>

  ### Starting backend
  1 - Create virtual environment to keep our dependeciens isolated and avoid packages conflicts
  
    python3 -m venv venv
    
  2 - activate virtual env 
    
     ubuntu/Mac -> "source venv/bin/activate"
     Win -> ".\venv\Scripts\activate"
     
  3 - Install DJango 
  
     $ python -m pip install Django
     
  4 - Install Django Rest framework
  
    $ pip install djangorestframework
    
  5 - Install corsheaders to request from  different domain than the one that served the web page (Frontend server != backend server)
  
    pip install django-cors-headers
    
  5 - Output a file to save/track our current packages
  
    $ pip freeze > requirements.txt
   Later we can install the same packages from it using : pip install -r requirements.txt
    
  6 - Start Django project
   
      $ django-admin startproject properties
      
 ### Setting up Django
  1 - Create an app for our API inside our project to separate it into different modules
  
      $ python manage.py startapp api 

  2 - Add Django rest framework and the api app we just created to our installed apps in properties/settings.py so Django can recognize it.
  
      INSTALLED_APPS = [
        'corsheaders',
        'api.apps.ApiConfig'
        'rest_framework',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
      ]
      
   3 - Insert corsheaders into our middleware
   
    MIDDLEWARE = 
    [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'corsheaders.middleware.CorsMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    
   4 - Set a permission to our front-end server

      CORS_ORIGIN_WHITELIST = [
         'http://localhost:8080',
      ]
   
      
  ### Setup SQLite DB
   1 - We will use SQlite for a small project. We need to make first migrations to setup the basic Django tables.
   
    $ python manage.py migrate
    
   2 - Create the models for the DB
   
        class Rooms(models.Model):
            ROOM_CHOICES = [
                ('kitchen', 'Kitchen'),
                ('bathroom', 'Bathroom'),
                ('bedroom', 'Bedroom'),
                ('living-room', 'Living Room'),
            ]
            name = models.CharField(max_length=50, choices=ROOM_CHOICES,)

            def __str__(self) -> str:
                return self.name

        class House(models.Model):
            name = models.CharField(max_length=50)

            def __str__(self) -> str:
                return self.name

        class House_Rooms(models.Model):
            house = models.ForeignKey(House, on_delete=models.CASCADE)
            room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
   
   3 - Migrate the newly written models
      
      $ python manage.py makemigrations
      $ python manage.py migrate
      
   ### Creating routes, views and serializers for our data
   Now that we have our models, we can start creating routes and views to create and modify the data in the DB.
   
   1 - We will start by creating routes for our API in the urls.py of our api folder/app.

      from django.urls import path
      from . import views
    
      urlpatterns = [
          path('houses', name='getHouses'),
          path('house/add', name='addHouse'),
          path('house/delete', name='deleteHouse'),
          path('house/update', name='updateHouse')
      ]
      
   2 - Now that we have the routes, we need some views , to handle what we will do once a user hits that point.
   
      from .models import House, Rooms , House_Rooms
      from .serializers import HouseSerializer, RoomSerializer
      from django.shortcuts import get_object_or_404
      from django.http import HttpResponse
      from rest_framework.response import Response
      from rest_framework.decorators import api_view
      from rest_framework import status
      import json

      @api_view(['GET'])
      def getData(request):
          houses = House.objects.all().order_by('name') 
          serializer = HouseSerializer(houses, many=True)
          return Response(serializer.data)

      @api_view(['GET','DELETE'])
      def deleteHouse(request):
          # Get the house ID from the request
          house_id = request.data.get('house_id')

          # Fetch Object
          house = get_object_or_404(House, pk=house_id)

          # Delete it
          house.delete()
          return Response(status=status.HTTP_202_ACCEPTED)

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

          return HttpResponse('House and rooms added successfully')

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

          return HttpResponse('House and rooms added successfully')
          
   3 - Now that we have our views, we need to assign them to each path:
   
    from django.urls import path
    from . import views

    urlpatterns = [
        path('houses',views.getData, name='getData'),
        path('addHouse',views.addHouse, name='addHouse'),
        path('house/delete', views.deleteHouse, name='deleteHouse'),
        path('house/update', views.updateHouse, name='updateHouse')
    ]
       

   3 - At our properties main folder, in urls.py entry point (root urls file), include the urls from our api. This will include all routes we establish on our api folder.
   
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('api/', include('api.urls'))
      ]

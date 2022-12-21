# Uniplaces exercise

Solving the first exercise sent from Uniplaces for Jr. Full Stack position

## The problem

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
    
## Solution process

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
    
  5 - Output a file to save/track our current packages
  
    $ pip freeze > requirements.txt
      #To install packages from it, we use : pip install -r requirements.txt
    
  6 - Start Django project
   
      $ django-admin startproject properties
      
 ### Setting up Django
  1 - Create an app for our API inside our project to separate it into different modules
  
      $ python manage.py startapp api 

  2 - Add Django rest framework and the api app we just created to our installed apps in properties/settings.py so Django can recognize it.
  
      INSTALLED_APPS = [
        'api.apps.ApiConfig'
        'rest_framework',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
      ]
   
   3 - On our main folder, on our urls.py entry point, include the url conf for our api. This will include all routes we establish on our api folder.
   
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('api.urls'))
    ]
      
  ### Setup SQLite DB
   1 - We will use SQlite for a small project. We need to make first migrations to setup the basic Django tables.
   
    $ python manage.py migrate
    
   2 - Create the models for the DB
   
        class Rooms(models.Model):
            name = models.CharField(max_length=50)

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

from django.urls import path
from . import views

urlpatterns = [
    path('houses', views.getHouses, name='getData'),
    path('house/add',views.addHouse, name='addHouse'),
    path('house/delete', views.deleteHouse, name='deleteHouse'),
    path('house/update', views.updateHouse, name='updateHouse')
]
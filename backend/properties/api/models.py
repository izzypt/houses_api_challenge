from django.db import models

# Create your models here.
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
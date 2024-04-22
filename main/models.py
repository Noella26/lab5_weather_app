from django.db import models

# Create your models here.
class weatherData(models.Model):
    City = models.CharField(max_length= 100)
    Country = models.CharField(max_length= 10)
    Coordinate = models.CharField(max_length= 40)
    Temperature = models.CharField(max_length = 40)
    Pressure = models.CharField(max_length = 40)
    Humidity = models.CharField(max_length = 40)
    Timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.

from django.db import models

class Passenger(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    identification_number = models.CharField(max_length=35) 

class Bus(models.Model):
    
    bus_unique_id = models.CharField(max_length=10,primary_key=True,unique=True)
    bus_class_type = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=10)
    arrival_city = models.CharField(max_length=10)
    date_of_departure =  models.DateField()
    time_of_departure = models.TimeField()

class Reservation(models.Model):

    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)




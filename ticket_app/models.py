from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Bus(models.Model):
    class Meta: 
        verbose_name_plural = "Bus"

    bus_id = models.CharField(max_length=10)
    bus_class_type = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=10)
    arrival_city = models.CharField(max_length=10)
    date_of_departure =  models.DateField()
    time_of_departure = models.TimeField()
    def __str__(self):
        return f"bus id : {self.bus_id} , \
            destination : {self.departure_city} to {self.arrival_city}, \
            date_of_departure: {self.date_of_departure}, \
            time_of_departure: {self.time_of_departure}"

class Passenger(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    identification_number = models.CharField(max_length=35) 

    def __str__(self):
        return f" name : {self.first_name} {self.last_name}"

class Reservation(models.Model):

    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE,related_name='_passenger')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,related_name='_bus')
    placed_at = models.DateTimeField(auto_now_add=True, null=True)
    number_of_seat_booked = models.SmallIntegerField()
    
    def __str__(self):
        return f" current reservation {self.number_of_seat_booked} , \
            passenger {self.passenger} , \
            bus_id : {self.bus.bus_id} , \
            departure : {self.bus.departure_city} , \
            arrival : {self.bus.arrival_city}"
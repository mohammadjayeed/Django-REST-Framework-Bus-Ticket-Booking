from django.db import models
from django.core.validators import MaxValueValidator

class Passenger(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    identification_number = models.CharField(max_length=35) 

    def __str__(self):
        return f"passenger name : {first_name} {last_name}"

class Bus(models.Model):

    bus_unique_id = models.CharField(max_length=10,primary_key=True,unique=True)
    bus_class_type = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=10)
    arrival_city = models.CharField(max_length=10)
    date_of_departure =  models.DateField()
    time_of_departure = models.TimeField()

    def __str__(self):
        return f"bus id : {bus_unique_id}"

class Reservation(models.Model):

    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f" passenger {passenger} ordered {placed_at}"

class SeatBooking(models.Model):

    reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    number_booked = models.SmallIntegerField(validators=[MaxValueValidator(35)])

    def __str__(self):
        return f"this reservation has {number_booked} number of booked reservations, bus : {bus} , reservation : { reservations}"




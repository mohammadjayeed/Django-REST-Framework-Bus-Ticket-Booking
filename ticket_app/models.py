from django.db import models
from django.core.validators import MaxValueValidator

class Bus(models.Model):

    
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

    # bus = models.ForeignKey(Bus,on_delete=models.SET_NULL,related_name='bus',null=True,blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    identification_number = models.CharField(max_length=35) 

    def __str__(self):
        return f" name : {self.first_name} {self.last_name}"


class Reservation(models.Model):

    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE,related_name='passenger')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,related_name='bus')
    placed_at = models.DateTimeField(auto_now_add=True, null=True)
    number_of_seat_booked = models.SmallIntegerField(validators=[MaxValueValidator(35)])
    

    def __str__(self):
        return f" current reservation {self.number_of_seat_booked}, after passenger {self.passenger} ordered around {self.placed_at.strftime('%Y-%m-%d %H:%M')}, bus_id : {self.bus.bus_id}"

# class SeatBooking(models.Model):

#     reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    
    

#     def __str__(self):
#         return f"this reservation has {self.number_booked} number of booked reservations, bus : {self.bus} , reservation : { self.reservations}"




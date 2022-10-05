from rest_framework import serializers
from ticket_app.models import *
from django.db.models import Sum

class BusSerializer(serializers.ModelSerializer):
    seat_booked = serializers.SerializerMethodField()
   
    
    class Meta:
        model = Bus
        fields = "__all__"

    def get_seat_booked(self,object):
        _value = Bus.objects.filter(id=object.id).aggregate(Sum('_bus__number_of_seat_booked'))
        return _value.values()

class PassengerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Passenger
        fields = "__all__"

























    # def save(self):
    #     print("HERE")
    #     print(Reservation.objects.filter(bus__bus_id='S27').aggregate(Sum('number_of_seat_booked')))
    #     if not self.number_of_seat_booked > 35:
    #         self.reservation = Reservation()
    #         self.reservation.save()


# class SeatBookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SeatBooking
#         fields = "__all__"
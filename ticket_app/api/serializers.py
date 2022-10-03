from rest_framework import serializers
from ticket_app.models import *

class BusSerializer(serializers.ModelSerializer):
    # passenger = PassengerSerializer(read_only=True,many=True)
    class Meta:
        model = Bus
        fields = ["bus_id","bus_class_type","departure_city","arrival_city"]

class PassengerSerializer(serializers.ModelSerializer):
    # bus = BusSerializer(read_only=True,many=True)
    class Meta:
        model = Passenger
        fields = "__all__"
    


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    bus = BusSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = ["passenger","number_of_seat_booked","bus"]


# class SeatBookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SeatBooking
#         fields = "__all__"
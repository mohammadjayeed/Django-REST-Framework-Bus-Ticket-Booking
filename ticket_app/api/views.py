from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ticket_app.models import *
from rest_framework.response import Response
from .serializers import *
from django.db.models import Sum


class PassengerViewSet(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class BusViewSet(ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class ReservationAPIView(APIView):

    def get(self,request):
        
        queryset = Reservation.objects.filter(bus__bus_id='S27').aggregate(Sum('number_of_seat_booked'))
        print(queryset)
        return Response({"1":"2"})
    
    

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


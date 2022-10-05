from django.db.models import Q, Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from ticket_app.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *


class PassengerViewSet(ReadOnlyModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class BusViewSet(ModelViewSet):
    queryset = Bus.objects.annotate(booked= Sum('_bus__number_of_seat_booked')).filter(Q(booked__lte=34) | Q(booked=None))
    serializer_class = BusSerializer


@api_view(['POST'])
def book_reservation(request):
    
    bus = Bus.objects.get(id=request.data['travel_id'])

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.last_name = request.data['last_name']
    passenger.email = request.data['email']
    passenger.mobile_number = request.data['mobile_number']
    passenger.identification_number = request.data['identification_number']
    passenger.save()

    reservation = Reservation()
    reservation.bus = bus
    reservation.passenger = passenger
    reservation.number_of_seat_booked = request.data['reservations']

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)




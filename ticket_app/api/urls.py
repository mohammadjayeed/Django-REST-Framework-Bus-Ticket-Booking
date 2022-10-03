from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('passenger',PassengerViewSet)
router.register('bus',BusViewSet)
router.register('reservation',ReservationViewSet)


urlpatterns = [
    
    path('',include(router.urls))
]
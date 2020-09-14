#from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from flights.models import Flight , Booking
from .serializers import ListSerializer ,ListSerializerBook
from django.utils import timezone
#from app_name.models import ModelName

class ListView(ListAPIView):
    #queryset = Booking.objects.all()
    queryset = Flight.objects.all()
    #queryset = Booking.objects.filter()
    serializer_class = ListSerializer


class ListViewbook(ListAPIView):
    #queryset = Booking.objects.all()
    queryset = Booking.objects.filter(date__gte=timezone.now())

    #queryset = Booking.objects.get(flight)
    serializer_class = ListSerializerBook

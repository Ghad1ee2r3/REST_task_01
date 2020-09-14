from rest_framework import serializers
from flights.models import Flight, Booking
#from .models import Flight, Booking

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id','destination', 'time', 'price']


class ListSerializerBook(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','flight', 'date']

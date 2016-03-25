__author__ = 'tanvir'

from rest_framework import serializers
from django.contrib.auth.models import User
from rides.models import TaxiLocation


class TaxiLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiLocation
        fields = ('id', 'driver', 'lat', 'lon')



class DriverResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiLocation
        fields = ('id', 'driver', 'lat', 'lon','status')


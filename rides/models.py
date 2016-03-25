from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TaxiLocation(models.Model):
    driver = models.OneToOneField(User, related_name='users')
    lon = models.FloatField()
    lat = models.FloatField()

    def __unicode__(self):
        return self.driver.username


class DriverResponse(models.Model):
    driver = models.OneToOneField(User, related_name='response_driver')
    lon = models.FloatField(default=0.0)
    lat = models.FloatField(default=0.0)
    status = models.BooleanField(default=True)


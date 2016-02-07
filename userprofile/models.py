from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from base.models import *


class UserProfile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    USERTYPE = (
        ('D', 'Driver'),
        ('P', 'passenger')
    )
    # base = models.ForeignKey(Base,null=True, blank=True)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone = models.IntegerField(max_length=300, null=True, blank=True)
    mobile = models.IntegerField(max_length=300, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='Male')
    nid = models.IntegerField(max_length=17, null=True, blank=True)
    profile_picture = models.ImageField(max_length=500, null=True, blank=True)
    nid_picture = models.ImageField(max_length=500, null=True, blank=True)
    gcm_register = models.IntegerField(max_length=500, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=200, choices=USERTYPE, default='Driver')
    # connected_user = models.OneToOneField(User, null=True, blank=True)
    connected_user = models.ForeignKey('auth.User', related_name='userprofiles', null=True, blank=True)

    def __unicode__(self):
        return self.first_name




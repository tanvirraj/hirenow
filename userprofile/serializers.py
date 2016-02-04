__author__ = 'tanvir'

from userprofile.models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'phone', 'mobile',
                  'date_of_birth', 'gender', 'nid', 'profile_picture', 'gcm_register', 'profession', 'user_type', 'connected_user'
        )


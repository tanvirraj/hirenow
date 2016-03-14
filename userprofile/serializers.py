__author__ = 'tanvir'

from userprofile.models import UserProfile

from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    connected_user = serializers.ReadOnlyField(source='connected_user.username')

    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'phone',
                  'mobile', 'date_of_birth', 'gender', 'nid', 'profile_picture',
                  'gcm_register', 'profession', 'user_type', 'connected_user', 
        )


class UserSerializer(serializers.ModelSerializer):

    userprofiles = UserProfileSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'is_active', 'userprofiles')
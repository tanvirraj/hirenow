from django.shortcuts import render

# Create your views here.

from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer , UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class UserProfileList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        userProfile = UserProfile.objects.all()
        serializer = UserProfileSerializer(userProfile, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        print request.data
        if serializer.is_valid():
            print "inside valid"
            print serializer
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(connected_user=self.request.username)


class UserProfileDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                  IsOwnerOrReadOnly,)

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        serializer = UserProfileSerializer(userProfile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        serializer = UserProfileSerializer(userProfile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        userProfile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

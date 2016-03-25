from django.shortcuts import render

# Create your views here.
from rides.models import TaxiLocation
from rides.serializers import TaxiLocationSerializer, DriverResponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userprofile.models import UserProfile
# cron job
from django_cron import CronJobBase, Schedule
from django.conf import settings
import urllib2
import json
import datetime
from django.contrib.sessions.backends.db import SessionStore
# corn job

from importlib import import_module
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore


class CheckDriverResponse(CronJobBase):
    # driver_response = DriverResponse.objects.all()
    now = datetime.datetime.now()
    RUN_AT_TIMES = ["6:20"]
    schedule = Schedule(run_at_times=RUN_AT_TIMES)


    def check_driver_response():
        print "hello World"
        pass



# gcm sender function


def make_request(alert_type, ticker, reg_ids, msg_data):
    print "Making Request now!"
    json_data = {
        "collapse_key" : alert_type,
        "data": {
            "data": msg_data,
            "ticker": ticker,

        },
        "registration_ids": reg_ids,
    }

    url = 'https://android.googleapis.com/gcm/send'
    myKey = "AIzaSyApEuSADq3aNG9cM21YDtdmooM_UvR0soI"
    data = json.dumps(json_data)
    headers = {'Content-Type': 'application/json', 'Authorization': 'key=%s'%myKey}
    req = urllib2.Request(url, data, headers)
    f = urllib2.urlopen(req)
    response = json.loads(f.read())
    print "Printing Response ....."
    # print response
    # print json.dumps(datas,default=json_util.default)
    # print json.dumps(response, sort_keys=True, indent=2 , default=json_util.default)
    return json.dumps(response, sort_keys=True, indent=2)



class TaxiLocationList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        taxiLocation = TaxiLocation.objects.all()
        serializer = TaxiLocationSerializer(taxiLocation, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaxiLocationSerializer(data=request.data)
        print request.data
        if serializer.is_valid():
            print "inside valid"
            print serializer
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TaxiLocationDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return TaxiLocation.objects.get(pk=pk)
        except TaxiLocation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        taxiLocation = self.get_object(pk)
        serializer = TaxiLocationSerializer(taxiLocation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # print "hello"
        # print request.user
        # user_profile= request.user.userprofiles
        # driver = user_profile.user_type
        # print driver
        # data = request.data
        # print data
        # # data["driver"]  = request.user.id
        taxiLocation = self.get_object(pk)
        serializer = TaxiLocationSerializer(taxiLocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        taxiLocation= self.get_object(pk)
        taxiLocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaxiSearchList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        get_lat = request.GET.get("lat", None)
        if get_lat:
            source_lat = float(get_lat)
        get_lon = request.GET.get("lon", None)
        if get_lon:
            source_lon = float(get_lon)


        destLat = request.GET.get("destLat", None)
        if destLat:
            destLat = float(destLat)
        destLon = request.GET.get("destLon", None)
        if destLon:
            destLon = float(destLon)


        step = 0
        for i in range(100):
            step = step + 1

            taxiLocation = TaxiLocation.objects.filter(lat=source_lat, lon=source_lon)
            if taxiLocation:
                break
            else:
                # There is no Taxi in this area
                taxiLocation = TaxiLocation.objects.filter(lat__gte=source_lat - (step * .05), lat__lte=source_lat + (step * .05),
                                                           lon__gte=source_lon - (step * .05), lon__lte=source_lon + (step * .05),
                                                           )



        if taxiLocation:
            for taxi in taxiLocation:
                        taxi_id = taxi.id
                        # print taxi_id
                        # print taxi.driver
                        user_profile = UserProfile.objects.get(connected_user=taxi.driver)
                        print "Printing User Profile"
                        gcm_register = user_profile.gcm_register
                        # print gcm_register
                        send_message = make_request("Hello %s " % user_profile.first_name,
                                                    "Do you want to go from %s,%s to %s,%s !" %(source_lat, source_lon, destLat, destLon),
                                                    [gcm_register],
                                                    # "http://khep.finder-lbs.com:8001"
                                                    "ride ")

                        print "hello world"
                        response_result= json.loads(send_message)
                        print response_result["success"]
                        if response_result["success"] == 1:
                            print "success ..."
                            # print taxiLocation
                            serializer = TaxiLocationSerializer(taxiLocation, many=True)
                            # print serializer.data
                            return Response(serializer.data)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# New Market  23.731128, 90.380206
# Gulsan 23.792496 90.407806
# Rampur 23.761226, 90.420766

driver_list = []

class DriverResponse(APIView):

    """
    List all snippets, or create a new snippet.
    """
    def post(self, request, format=None):
        data = request.data
        serializer = DriverResponseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            CheckDriverResponse()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)






            # driver_id = driver.id
            # if driver_id:
            #     driver_list.append(driver)
            #     request.session['driver_list'] = driver_list
            #     d_list = request.session['driver_list']
            #     print d_list

                #
                #
                # user_profile = UserProfile.objects.get(connected_user=driver_id)
                # driver_name = user_profile.username
                #
                # passenger_user_profile = request.user.userprofiles
                # passenger_gcm_register =  passenger_user_profile.gcm_register
                #
                # send_message = make_request("Hello %s " % user_profile.first_name,
                #                                     "Do you want to go from %s,%s to %s,%s !" % (source_lat, source_lon, dest_lat, dest_lon),
                #                                     [gcm_register],
                #                                     # "http://khep.finder-lbs.com:8001"
                #                                     data)
                # if response_result["success"] == 1:
                #     print "success ..."
                #     # print taxiLocation
            #     return Response(status=status.HTTP_200_OK)
            # else:
            #     return Response(status=status.HTTP_400_BAD_REQUEST)


    # def post(self, request, format=None):
    #     data = request.data
    #     for driver in data:
    #         driver_id = driver.id
    #
    #         if driver_id:
    #             user_profile = UserProfile.objects.get(connected_user=driver_id)
    #             driver_name = user_profile.username
    #             passenger_user_profile = request.user.userprofiles
    #             passenger_gcm_register =  passenger_user_profile.gcm_register
    #             send_message = make_request("Hello %s " % user_profile.username,
    #                                                 "Do you want to go from %s,%s to %s,%s !" % (source_lat, source_lon, dest_lat, dest_lon),
    #                                                 [gcm_register],
    #                                                 # "http://khep.finder-lbs.com:8001"
    #                                                 data)
    #
    #
    #
    #     serializer = TaxiLocationSerializer(data=request.data)
    #     print request.data
    #     if serializer.is_valid():
    #         print "inside valid"
    #         print serializer
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #



from django.shortcuts import render

# Create your views here.
from rides.models import TaxiLocation
from rides.serializers import TaxiLocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userprofile.models import UserProfile

import urllib2
import json
# from bson import json_util

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
        user_profile= request.user.userprofiles
        # driver = user_profile.user_type
        # print driver
        # data = request.data
        # print data
        # # data["driver"]  = request.user.id
        taxiLocation = self.get_object(pk)
        serializer = TaxiLocationSerializer(taxiLocation, data=data)
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
            lat = float(get_lat)
        get_lon = request.GET.get("lon", None)
        if get_lon:
            lon = float(get_lon)
            print type(lon)



        # driver = request.GET.get(driver, None)

        from_location = request.GET.get("from_location", None)
        to_locaton = request.GET.get("to_location", None)
        # print from_location
        # print to_locaton
        step = 0
        for i in range(100):
            step = step + 1
            # taxiLocation = TaxiLocation.objects.filter(lat__gte=lat - (step * .05), lat__lte=lat + (step * .05),
            # lon__gte=lon - (step * .05), lon__lte=lon + (step * .05),driver=driver)

            taxiLocation = TaxiLocation.objects.filter(lat=lat, lon=lon)
            if taxiLocation:
                break


            else:
                # There is no Taxi in this area
                taxiLocation = TaxiLocation.objects.filter(lat__gte=lat - (step * .05), lat__lte=lat + (step * .05),
                                                           lon__gte=lon - (step * .05), lon__lte=lon + (step * .05),
                                                           )


                # else:
                #     agencies = Agency.objects.filter(postal_code__icontains=search,
                #                                      servicetype__name=search_label) | Agency.objects.filter(
                #         street_address__icontains=search, servicetype__name=search_label) | Agency.objects.filter(
                #         lat__gte=lat - (step * .05),
                #         lat__lte=lat + (step * .05),
                #         lon__gte=lon - (step * .05),
                #         lon__lte=lon + (step * .05), servicetype__name=search_label)
                # agencies = Agency.objects.get(
                # Q(zip_code__icontains=search) | Q(address__icontains=search) | Q(lat__gte=lat-1.05, lat__lte=lat+1.05, lon__gte=lon-1.05, lon__lte=lon+1.05)
                #     )
        if taxiLocation:
            for taxi in taxiLocation:
                        taxi_id = taxi.id
                        # print taxi_id
                        # print taxi.driver
                        user_profile = UserProfile.objects.get(connected_user=taxi.driver)
                        print "Printing User Profile"
                        gcm_register = user_profile.gcm_register
                        # print gcm_register
                        send_message = make_request("Dear%s !"% user_profile.first_name,
                                                    "Do you want to go from %s to %s !"%(from_location , to_locaton),
                                                    [gcm_register],
                                                    # "http://khep.finder-lbs.com:8001"
                                                    "hello ")

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


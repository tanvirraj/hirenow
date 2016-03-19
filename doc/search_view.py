__author__ = 'tanvir'


class AgencyList(APIView):
    def get(self, request, format=None):
        search = request.GET.get("search", None)
        address = request.GET.get("address", None)
        search_label = request.GET.get("label", None)
        print "Search label", search_label, search, address
        """
        ServiceType
        name=models.CharField(max_length=200, blank=True, null=True)
        agencies = models.ManyToManyField(Agency)
        """

        lat = request.GET.get("lat", None)

        if lat is not None:
            lat = float(lat)
        lon = request.GET.get("lon", None)
        if lon is not None:
            lon = float(lon)
        count = request.GET.get("count", None)
        print "Lat:Lon", lat, lon
        if lat is not None and lon is not None:
            # agencies = Agency.objects.filter(zip_code__contains=search,lat__gte=lat-.05, lat__lte=lat+.05, lon__gte=lon-.05, lon__lte=lon+.05) | Agency.objects.filter(address__contains=search,lat__gte=lat-.05, lat__lte=lat+.05, lon__gte=lon-.05, lon__lte=lon+.05)
            agencies = Agency.objects.filter(street_address__icontains=search,
                                             servicetype__name=search_label) | Agency.objects.filter(
                address_location__icontains=search, servicetype__name=search_label)

            # agencies = Agency.objects.filter(zip_code__icontains=search) | Agency.objects.filter(address__icontains=search) | Agency.objects.filter(lat__gte=lat-1.05, lat__lte=lat+1.05, lon__gte=lon-1.05, lon__lte=lon+1.05)


            step = 0
            for i in range(100):
                step = step + 1
                print step
                if agencies.count() > 0:
                    agencies = agencies.filter(lat__gte=lat - (step * .05), lat__lte=lat + (step * .05),
                                               lon__gte=lon - (step * .05), lon__lte=lon + (step * .05),
                                               servicetype__name=search_label)
                    break
                else:
                    agencies = Agency.objects.filter(postal_code__icontains=search,
                                                     servicetype__name=search_label) | Agency.objects.filter(
                        street_address__icontains=search, servicetype__name=search_label) | Agency.objects.filter(
                        lat__gte=lat - (step * .05),
                        lat__lte=lat + (step * .05),
                        lon__gte=lon - (step * .05),
                        lon__lte=lon + (step * .05), servicetype__name=search_label)
            # agencies = Agency.objects.get(
            # Q(zip_code__icontains=search) | Q(address__icontains=search) | Q(lat__gte=lat-1.05, lat__lte=lat+1.05, lon__gte=lon-1.05, lon__lte=lon+1.05)
            #     )
            print agencies
            print "Inside lat lon as not None"
        else:

            if search is None or search == "":
                if address is not None:
                    agencies = Agency.objects.filter(address_location__icontains=address,
                                                     servicetype__name=search_label) | Agency.objects.filter(
                        street_address__icontains=address, servicetype__name=search_label)
                else:
                    agencies = Agency.objects.all()
            else:
                if lat is not None and lon is not None:

                    # agencies = Agency.objects.filter(zip_code__contains=search,lat__gte=lat-.05, lat__lte=lat+.05, lon__gte=lon-.05, lon__lte=lon+.05) | Agency.objects.filter(address__contains=search,lat__gte=lat-.05, lat__lte=lat+.05, lon__gte=lon-.05, lon__lte=lon+.05)
                    agencies = Agency.objects.filter(street_address__icontains=search,
                                                     servicetype__name=search_label) | Agency.objects.filter(
                        address_location__icontains=search, servicetype__name=search_label)

                    # agencies = Agency.objects.filter(zip_code__icontains=search) | Agency.objects.filter(address__icontains=search) | Agency.objects.filter(lat__gte=lat-1.05, lat__lte=lat+1.05, lon__gte=lon-1.05, lon__lte=lon+1.05)


                    step = 0
                    for i in range(100):
                        step = step + 1
                        if agencies.count() > 0:
                            agencies = agencies.filter(lat__gte=lat - (step * .05), lat__lte=lat + (step * .05),
                                                       lon__gte=lon - (step * .05), lon__lte=lon + (step * .05),
                                                       servicetype__name=search_label)
                            break
                        else:
                            agencies = Agency.objects.filter(postal_code__icontains=search,
                                                             servicetype__name=search_label) | Agency.objects.filter(
                                street_address__icontains=search,
                                servicetype__name=search_label) | Agency.objects.filter(lat__gte=lat - (step * .05),
                                                                                        lat__lte=lat + (step * .05),
                                                                                        lon__gte=lon - (step * .05),
                                                                                        lon__lte=lon + (step * .05),
                                                                                        servicetype__name=search_label)
                    # agencies = Agency.objects.get(
                    # Q(zip_code__icontains=search) | Q(address__icontains=search) | Q(lat__gte=lat-1.05, lat__lte=lat+1.05, lon__gte=lon-1.05, lon__lte=lon+1.05)
                    #     )
                    print agencies
                    print "Inside lat lon as not None"
                else:
                    agencies = Agency.objects.filter(postal_code__icontains=search,
                                                     servicetype__name=search_label) | Agency.objects.filter(
                        address_location__icontains=search, servicetype__name=search_label) | Agency.objects.filter(
                        mail_address__icontains=search, servicetype__name=search_label) | Agency.objects.filter(
                        street_address__icontains=search, servicetype__name=search_label)
                    # agencies = Agency.objects.get(
                    # Q(zip_code__icontains=search) | Q(address__icontains=search)
                    #     )
                    print "Inside lat lon as None"
        if count is None:
            serializer = PaginatedAgencySerializer(agencies, request, 30)

        else:
            serializer = PaginatedAgencySerializer(agencies, request, count)
        return Response(serializer.data)

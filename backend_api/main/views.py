from django.shortcuts import render
from . import serializer
from . import models
from rest_framework import generics
# Create your views here.
class VendorList(generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    # print(queryset)
    serializer_class = serializer.VendorSerializer
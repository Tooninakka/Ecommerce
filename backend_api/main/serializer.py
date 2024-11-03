from rest_framework import serializers
from . import models

class VendorSerializer(serializers.Serializer):
    class Meta:
        model = models.Vendor
        fields = ['user', 'address', ]
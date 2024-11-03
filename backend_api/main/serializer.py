from rest_framework import serializers
from . import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address', ]
        
        def __init__(self):
            super(VendorSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            self.Meta.depth = 1
    
class VendorDetailSerializer(serializers.HyperlinkedRelatedField):
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address', ]
        
        def __init__(self):
            super(VendorDetailSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            self.Meta.depth = 1

class ProductCategorySerializer(serializers.Serializer):
    class Meta:
        model = models.ProductCategory
        fields = ['id', 'title', 'detail', ]

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'category', 'vendor', 'detail', 'price', ]
        
        def __init__(self):
            super(ProductListSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            self.Meta.depth = 1

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'category', 'vendor', 'detail', 'price', ]
        
        def __init__(self):
            super(ProductDetailSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            self.Meta.depth = 1

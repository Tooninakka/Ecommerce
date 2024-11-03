from django.urls import path
from . import views
urlpatterns = [
    path('vendors/', views.VendorList.as_view(), name='vendor'),
    path('vendor/<int:pk>', views.VendorList.as_view(), name='vendor_details'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='products'),
]

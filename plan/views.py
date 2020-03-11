from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.mixins import (ListModelMixin,
                                RetrieveModelMixin,
                                UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated                                
from plan.models import Merchant, Store, Item
from plan.serializers import (MerchantSerializer,
                            StoreSerializer,
                            ItemSerializer)

# Create your views here.

class MerchantViewSet(viewsets.ModelViewSet,
                    UpdateModelMixin):
    permission_classes = (IsAuthenticated, )                
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class StoreViewSet(viewsets.ModelViewSet,
                UpdateModelMixin):                   
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ItemViewSet(viewsets.ModelViewSet,
                UpdateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer    
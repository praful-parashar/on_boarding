import json
import structlog
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, serializers
from rest_framework import permissions
from rest_framework.mixins import (ListModelMixin,
                                RetrieveModelMixin,
                                UpdateModelMixin)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated   
from celery.task import task 
from plan.tasks import *                            
from plan.models import *
from plan.serializers import (MerchantSerializer,
                            StoreSerializer,
                            ItemSerializer,
                            TransactionSerializer)

# Create your views here.
logger = structlog.getLogger(__name__)
class MerchantViewSet(viewsets.ModelViewSet,
                    UpdateModelMixin):
    permission_classes = (IsAuthenticated, )                
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_class

    @action(detail=True, methods=['get'])
    def stores(self, request, pk=None):
        try:
            merchant = Merchant.objects.get(pk=pk)
            stores_queryset = Store.objects.filter(merchant=merchant)
            serializer = StoreSerializer(stores_queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return str(e)

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        try: 
            merchant = Merchant.objects.get(pk=pk)
            items_queryset = merchant.merchant_items.all()
            page = self.paginate_queryset(list(items_queryset))
            if page is not None:
                serializer = ItemSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = ItemSerializer(items_queryset, many=True)    
            return Response(serializer.data)
        except Exception as e:
            return str(e)  

    @action(detail=True, methods=['get'])
    def transactions(self, request, pk=None):
        try:
            merchant = Merchant.objects.get(pk=pk)
            txs_queryset = merchant.merchant_transactions.all()
            serializer = TransactionSerializer(txs_queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return str(e)        


class StoreViewSet(viewsets.ModelViewSet,
                UpdateModelMixin): 
    permission_classes = (IsAuthenticated, )                   
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    @action(detail=True, methods=['get'])
    def transactions(self, request, pk=None):
        try:
            store = Store.objects.get(pk=pk)
            txs_queryset = store.store_transactions.all()
            serializer = TransactionSerializer(txs_queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return str(e)


class ItemViewSet(viewsets.ModelViewSet,
                UpdateModelMixin):
    permission_classes = (IsAuthenticated, ) 
    queryset = Item.objects.all()
    serializer_class = ItemSerializer 

    @action(detail=True, methods=['get'])
    def merchant(self, request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
            serializer = MerchantSerializer(item.merchant, many=False)
            return Response(serializer.data)
        except Exception as e:
            return str(e)   


class TransactionViewSet(viewsets.ModelViewSet,
                        UpdateModelMixin):                        
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer 

    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            foo = create_txs.delay(serializer.data)
        
        return Response("Transaction is queued, refresh and verify")

                               
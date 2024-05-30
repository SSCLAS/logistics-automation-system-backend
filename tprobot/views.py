from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Robot, Product, Ware_house, Deliver_order, Stock_order
from .serializers import RobotSerializer, ProductSerializer, Ware_houseSerializer, Deliver_orderSerializer, Stock_orderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

class DeliverCreateView(CreateAPIView):
    queryset = Deliver_order.objects.all()
    serializer_class = Deliver_orderSerializer

class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Ware_houseViewSet(viewsets.ModelViewSet):
    queryset = Ware_house.objects.all()
    serializer_class = Ware_houseSerializer
class Deliver_orderViewSet(viewsets.ModelViewSet):
    queryset = Deliver_order.objects.all()
    serializer_class = Deliver_orderSerializer

class Stock_orderViewSet(viewsets.ModelViewSet):
    queryset = Stock_order.objects.all()
    serializer_class = Stock_orderSerializer



#class ProductListAPI(APIView):
#     def get(self, request):
#         queryset = Product.objects.all()
#         print(queryset)
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
    
# class RobotListAPI(APIView):
#     def get(self, request):
#         queryset = Robot.objects.all()
#         print(queryset)
#         serializer = RobotSerializer(queryset, many = True)
#         return Response(serializer.data)
    
# class Ware_houseListAPI(APIView):
#     def get(self, request):
#         queryset = Ware_house.objects.all()
#         print(queryset)
#         serializer = Ware_houseSerializer(queryset, many = True)
#         return Response(serializer.data)
    
# class Deliver_orderListAPI(APIView):
#     def get(self, request):
#         queryset = Deliver_order.objects.all()
#         print(queryset)
#         serializer = Deliver_orderSerializer(queryset, many = True)
#         return Response(serializer.data)
    
# class Stock_orderListAPI(APIView):
#     def get(self, request):
#         queryset = Stock_order.objects.all()
#         print(queryset)
#         serializer = Stock_orderSerializer(queryset, many = True)
#         return Response(serializer.data)
    



from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Robot
from .models import Product
from .models import Ware_house
from .models import Deliver_order
from .models import Stock_order

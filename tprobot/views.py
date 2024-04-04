from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import robot
from .models import product
from .models import ware_house
from .models import deliver_order
from .models import stock_order

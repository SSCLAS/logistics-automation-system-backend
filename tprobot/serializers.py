from rest_framework import serializers
from .models import Robot, Product, Ware_house, Deliver_order, Stock_order

class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class Ware_houseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ware_house
        fields = "__all__"

class Deliver_orderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deliver_order
        fields = "__all__"

class Stock_orderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stock_order
        fields = "__all__"


#####################  hyperlinkedserializer   #####################
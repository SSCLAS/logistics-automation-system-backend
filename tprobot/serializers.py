from rest_framework import serializers
from .models import Robot, Product, Ware_house, Deliver_order, Stock_order

class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    ware_house_product = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ware_house-detail'
    )

    class Meta:
        model = Product
        fields = ['url', 'product_name', 'product_date', 'product_manufacture', 
                  'product_price','ware_house_product']

class Ware_houseSerializer(serializers.HyperlinkedModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_date = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField() 
    deliver_ordered = serializers.SerializerMethodField()

    class Meta:
        model = Ware_house
        fields = "__all__"

    def get_deliver_ordered(self, obj):
        if obj.product_id is not None:
            try:
                item = Deliver_order.objects.get(product_id=obj.product_id.pk)
            except Deliver_order.DoesNotExist:
                item = None

            if item is not None:
                return item.deliver_order_processing
            else:
                return
        else:
            return

    def get_product_name(self, obj):
        if obj.product_id is not None:
            return obj.product_id.product_name
        
    def get_product_date(self, obj):
        if obj.product_id is not None:
            return obj.product_id.product_date
        
    def get_product_price(self, obj):
        if obj.product_id is not None:
            return obj.product_id.product_price
    

class Deliver_orderSerializer(serializers.HyperlinkedModelSerializer):
    ware_house_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Deliver_order
        fields = "__all__"

    def get_ware_house_name(self, obj):
        if obj.product_id is not None:
            try:
                item = Ware_house.objects.get(product_id=obj.product_id.pk)
            except Ware_house.DoesNotExist:
                item = None    
                
            if item is not None:
                return item.ware_house_name
            else:
                return 
        else:  
            return 

class Stock_orderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stock_order
        fields = "__all__"


#####################  hyperlinkedserializer   #####################
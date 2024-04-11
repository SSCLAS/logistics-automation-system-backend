from django.db import models

# Create your models here.
class Robot(models.Model):
    robot_name = models.CharField(max_length=200)
    robot_status = models.BooleanField(default= False)

    def __str__(self) -> str:
        return self.robot_name
    
    # def get_route(self):
    #     route = []
    #     data = self.station_route.all()
    #     for i in data:
    #         route.append(i.route.route_name)
    #     return route
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_date = models.DateTimeField('생산날짜')
    product_manufacture = models.CharField(max_length=200)
    product_price = models.FloatField()
    #사이즈나 무게가 입력되어야하는 제품 선택해서 입력하게 할 수 있는 방법 찾기
    def __str__(self) -> str:
        return self.product_name
    
class Ware_house(models.Model):
    ware_house_Width = models.DecimalField(max_digits= 10, decimal_places=2)
    ware_house_height = models.DecimalField(max_digits= 10, decimal_places=2)
    ware_house_length = models.DecimalField(max_digits= 10, decimal_places=2) 
    ware_house_status = models.BooleanField(default=False) 
    ware_house_location_x = models.FloatField()
    ware_house_location_y = models.FloatField()
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='Ware_house')

class Deliver_order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name= 'Deliver_order')
    deliver_order_order_date = models.DateTimeField('입고 명령 일자')
    deliver_order_processing = models.BooleanField(default=False)
    deliver_order_complete_date = models.DateTimeField('입고 완료 일자', null=True)
    robot_id = models.ForeignKey(Robot, on_delete=models.PROTECT, related_name= 'Deliver_order')

class Stock_order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='Stock_order')
    stock_order_order_date = models.DateTimeField('출고 명령 일자')
    stock_order_processing = models.BooleanField(default=False)
    stock_order_complete_date = models.DateTimeField('출고 완료 일자', null=True)
    ware_house_id = models.ForeignKey(Ware_house, on_delete=models.PROTECT, related_name='Stock_order')



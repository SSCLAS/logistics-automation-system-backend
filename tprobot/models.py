from django.db import models

# Create your models here.
class robot(models.Model):
    r_name = models.CharField(max_length=200)
    r_status = models.BooleanField(default= False)

    def __str__(self) -> str:
        return self.r_name
    
class product(models.Model):
    p_name = models.CharField(max_length=200)
    p_date = models.DateTimeField('생산날짜')
    p_manufacture = models.CharField(max_length=200)
    p_price = models.FloatField()
    #사이즈나 무게가 입력되어야하는 제품 선택해서 입력하게 할 수 있는 방법 찾기
    def __str__(self) -> str:
        return self.p_name
    
class ware_house(models.Model):
    w_Width = models.DecimalField(max_digits= 10, decimal_places=2)
    w_height = models.DecimalField(max_digits= 10, decimal_places=2)
    w_length = models.DecimalField(max_digits= 10, decimal_places=2) 
    w_status = models.BooleanField(default=False) 
    w_location_x = models.FloatField()
    w_location_y = models.FloatField()
    product_id = models.ForeignKey(product, on_delete=models.PROTECT, related_name='ware_house')

class deliver_order(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.PROTECT, related_name= 'deliver_order')
    d_order_date = models.DateTimeField('입고 명령 일자')
    d_processing = models.BooleanField(default=False)
    d_complete_date = models.DateTimeField('입고 완료 일자')
    robot_id = models.ForeignKey(robot, on_delete=models.PROTECT, related_name= 'deliver_order')

class stock_order(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.PROTECT, related_name='stock_order')
    s_order_date = models.DateTimeField('출고 명령 일자')
    s_processing = models.BooleanField(default=False)
    s_complete_date = models.DateTimeField('출고 완료 일자')
    ware_house_id = models.ForeignKey(ware_house, on_delete=models.PROTECT, related_name='stock_order')



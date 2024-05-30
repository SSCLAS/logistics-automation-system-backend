from django.db import models

# Create your models here.
class Robot(models.Model):
    robot_name = models.CharField(max_length=200)
    robot_status = models.BooleanField(default= False)
    robot_image = models.ImageField(upload_to='robots', null=True)

    def __str__(self) -> str:
        return self.robot_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_date = models.DateTimeField('생산날짜', auto_now_add=True)
    product_manufacture = models.CharField(max_length=200, default='SSC철강')
    product_price = models.FloatField(default=10000.0)
    #사이즈나 무게가 입력되어야하는 제품 선택해서 입력하게 할 수 있는 방법 찾기
    def __str__(self) -> str:
        return f'{self.product_name}'
    
class Ware_house(models.Model):
    ware_house_name = models.CharField(max_length=5, null=True)
    ware_house_Width = models.DecimalField(max_digits= 10, decimal_places=2)
    ware_house_height = models.DecimalField(max_digits= 10, decimal_places=2)
    ware_house_length = models.DecimalField(max_digits= 10, decimal_places=2) 
    
    ware_house_status = models.BooleanField(default=False) 
    
    ware_house_location_x = models.FloatField()
    ware_house_location_y = models.FloatField()
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='ware_house_product', null=True, blank=True)
    #deliver_order_date = models.BooleanField(default=False) # 상기랑 확인


    def __str__(self) -> str:
        return self.ware_house_name
    
# admin사이트에서 product_id 빈칸으로 창고 만들수있게 하기

class Deliver_order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name= 'Deliver_product')
    deliver_order_order_date = models.DateTimeField('출고 명령 일자', auto_now_add=True)
    deliver_order_processing = models.CharField(max_length=1, default='B')
    deliver_order_complete_date = models.DateTimeField('출고 완료 일자', null=True, blank=True)
    robot_id = models.ForeignKey(Robot, on_delete=models.PROTECT, related_name= 'Deliver_robot', default = 'http://127.0.0.1:8000/Robot/1/')
    # ware_house_id = models.ForeignKey(Ware_house, on_delete=models.PROTECT, related_name='Deliver_order',  null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.deliver_order_complete_date is not None:
            ware_house = Ware_house.objects.get(product_id=self.product_id.pk)
            ware_house.ware_house_status = False
            ware_house.product_id = None
            ware_house.save(update_fields=['ware_house_status', 'product_id'])
        super().save(*args, **kwargs) 
        
        
class Stock_order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='Stock_product')
    stock_order_order_date = models.DateTimeField('입고 명령 일자', auto_now_add=True)
    stock_order_processing = models.BooleanField(default=False)
    stock_order_complete_date = models.DateTimeField('입고 완료 일자', null=True, blank=True)
    ware_house_id = models.ForeignKey(Ware_house, on_delete=models.PROTECT, related_name='Stock_order',  null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.ware_house_id is not None:
            ware_house = Ware_house.objects.get(id=self.ware_house_id.pk)
            ware_house.ware_house_status = True
            ware_house.product_id = self.product_id
            ware_house.save(update_fields=['ware_house_status', 'product_id'])
        super().save(*args, **kwargs) 
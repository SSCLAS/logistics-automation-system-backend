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
    p_origin = models.CharField(max_length=200)
    p_price = models.FloatField()
    
    def __str__(self) -> str:
        return self.p_name
    
class ware_house(models.Model):
    w_Width = models.DecimalField(max_digits= 10, decimal_places=2)
    w_height = models.DecimalField(max_digits= 10, decimal_places=2)
    w_length = models.DecimalField(max_digits= 10, decimal_places=2) 
    w_status = models.BooleanField(default=False) 


class detail(models.Model):
    d_store = models.IntegerField()
    d_release = models.IntegerField()
    d_date = models.DateTimeField('입출고 날짜 및 시간')
    product_id = models.ForeignKey(product, on_delete=models.PROTECT, related_name = 'detail')
    robot_id = models.ForeignKey(robot, on_delete=models.PROTECT, related_name = 'detail')
    ware_house_id = models.ForeignKey(ware_house, on_delete=models.PROTECT, related_name = 'detail')

    def __str__(self) -> str:
        return self.robot_id.r_name


from django.contrib import admin

# Register your models here.
from .models import Robot
from .models import Product
from .models import Deliver_order
from .models import Stock_order
from .models import Ware_house




admin.site.register(Robot)
admin.site.register(Product)
admin.site.register(Deliver_order)
admin.site.register(Stock_order)
admin.site.register(Ware_house)
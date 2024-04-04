from django.contrib import admin

# Register your models here.
from .models import robot
from .models import product
from .models import deliver_order
from .models import stock_order
from .models import ware_house




admin.site.register(robot)
admin.site.register(product)
admin.site.register(deliver_order)
admin.site.register(stock_order)
admin.site.register(ware_house)
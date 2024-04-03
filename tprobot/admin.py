from django.contrib import admin

# Register your models here.
from .models import robot
from .models import product
from .models import detail
from .models import ware_house




admin.site.register(robot)
admin.site.register(product)
admin.site.register(detail)
admin.site.register(ware_house)
from django.contrib import admin

# Register your models here.
from .models import Robot, Product, Deliver_order, Stock_order, Ware_house

admin.site.register(Robot) 

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_date", "product_manufacture",]

admin.site.register(Product, ProductAdmin)

class Deliver_order_Admin(admin.ModelAdmin):
    list_display = ['product_id', 'deliver_order_order_date', 'deliver_order_processing','deliver_order_complete_date', 'robot_id']

admin.site.register(Deliver_order, Deliver_order_Admin)


admin.site.register(Stock_order)
admin.site.register(Ware_house)
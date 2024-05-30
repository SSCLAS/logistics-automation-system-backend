from django.contrib import admin

# Register your models here.
from .models import Robot, Product, Deliver_order, Stock_order, Ware_house


class Robot_admin(admin.ModelAdmin):
    list_display = ['robot_name', 'robot_status']

admin.site.register(Robot, Robot_admin) 

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "product_date", "product_manufacture",]

admin.site.register(Product, ProductAdmin)

class Deliver_order_Admin(admin.ModelAdmin):
    list_display = ['product_id', 'deliver_order_order_date', 'deliver_order_processing','deliver_order_complete_date', 'robot_id']

admin.site.register(Deliver_order, Deliver_order_Admin)

class Stock_order_Admin(admin.ModelAdmin):
    list_display = ['product_id', 'stock_order_order_date', 'stock_order_processing', 'stock_order_complete_date', 'ware_house_id']

admin.site.register(Stock_order, Stock_order_Admin)

class Ware_house_Admin(admin.ModelAdmin):
    list_display = ['ware_house_name','ware_house_Width','ware_house_height', 'ware_house_length', 'ware_house_status', 'product_id']

admin.site.register(Ware_house,Ware_house_Admin)

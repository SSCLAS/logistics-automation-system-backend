# Generated by Django 5.0.3 on 2024-04-10 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tprobot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliver_order',
            old_name='d_complete_date',
            new_name='deliver_order_complete_date',
        ),
        migrations.RenameField(
            model_name='deliver_order',
            old_name='d_order_date',
            new_name='deliver_order_order_date',
        ),
        migrations.RenameField(
            model_name='deliver_order',
            old_name='d_processing',
            new_name='deliver_order_processing',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='p_date',
            new_name='product_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='p_manufacture',
            new_name='product_manufacture',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='p_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='p_price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='robot',
            old_name='r_name',
            new_name='robot_name',
        ),
        migrations.RenameField(
            model_name='robot',
            old_name='r_status',
            new_name='robot_status',
        ),
        migrations.RenameField(
            model_name='stock_order',
            old_name='s_complete_date',
            new_name='stock_order_complete_date',
        ),
        migrations.RenameField(
            model_name='stock_order',
            old_name='s_order_date',
            new_name='stock_order_order_date',
        ),
        migrations.RenameField(
            model_name='stock_order',
            old_name='s_processing',
            new_name='stock_order_processing',
        ),
        migrations.RenameField(
            model_name='ware_house',
            old_name='w_Width',
            new_name='ware_house_Width',
        ),
        migrations.RenameField(
            model_name='ware_house',
            old_name='w_height',
            new_name='ware_house_height',
        ),
        migrations.RenameField(
            model_name='ware_house',
            old_name='w_length',
            new_name='ware_house_length',
        ),
        migrations.RenameField(
            model_name='ware_house',
            old_name='w_location_x',
            new_name='ware_house_location_x',
        ),
        migrations.RenameField(
            model_name='ware_house',
            old_name='w_location_y',
            new_name='ware_house_location_y',
        ),
        migrations.RenameField(
            model_name='ware_house',
            old_name='w_status',
            new_name='ware_house_status',
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-11 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_date', models.DateTimeField(verbose_name='생산날짜')),
                ('product_manufacture', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot_name', models.CharField(max_length=200)),
                ('robot_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Deliver_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver_order_order_date', models.DateTimeField(verbose_name='입고 명령 일자')),
                ('deliver_order_processing', models.BooleanField(default=False)),
                ('deliver_order_complete_date', models.DateTimeField(verbose_name='입고 완료 일자')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Deliver_order', to='tprobot.product')),
                ('robot_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Deliver_order', to='tprobot.robot')),
            ],
        ),
        migrations.CreateModel(
            name='Ware_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ware_house_Width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ware_house_height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ware_house_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ware_house_status', models.BooleanField(default=False)),
                ('ware_house_location_x', models.FloatField()),
                ('ware_house_location_y', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Ware_house', to='tprobot.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_order_order_date', models.DateTimeField(verbose_name='출고 명령 일자')),
                ('stock_order_processing', models.BooleanField(default=False)),
                ('stock_order_complete_date', models.DateTimeField(verbose_name='출고 완료 일자')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Stock_order', to='tprobot.product')),
                ('ware_house_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Stock_order', to='tprobot.ware_house')),
            ],
        ),
    ]

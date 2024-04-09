# Generated by Django 5.0.3 on 2024-04-09 21:57

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
                ('p_name', models.CharField(max_length=200)),
                ('p_date', models.DateTimeField(verbose_name='생산날짜')),
                ('p_manufacture', models.CharField(max_length=200)),
                ('p_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=200)),
                ('r_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Deliver_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_order_date', models.DateTimeField(verbose_name='입고 명령 일자')),
                ('d_processing', models.BooleanField(default=False)),
                ('d_complete_date', models.DateTimeField(verbose_name='입고 완료 일자')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Deliver_order', to='tprobot.product')),
                ('robot_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Deliver_order', to='tprobot.robot')),
            ],
        ),
        migrations.CreateModel(
            name='Ware_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_Width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('w_height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('w_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('w_status', models.BooleanField(default=False)),
                ('w_location_x', models.FloatField()),
                ('w_location_y', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Ware_house', to='tprobot.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_order_date', models.DateTimeField(verbose_name='출고 명령 일자')),
                ('s_processing', models.BooleanField(default=False)),
                ('s_complete_date', models.DateTimeField(verbose_name='출고 완료 일자')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Stock_order', to='tprobot.product')),
                ('ware_house_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Stock_order', to='tprobot.ware_house')),
            ],
        ),
    ]

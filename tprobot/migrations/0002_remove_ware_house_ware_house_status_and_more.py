# Generated by Django 5.0 on 2024-05-30 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tprobot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ware_house',
            name='ware_house_status',
        ),
        migrations.AlterField(
            model_name='deliver_order',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Deliver_product', to='tprobot.product', unique=True),
        ),
    ]

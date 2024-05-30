# Generated by Django 5.0 on 2024-05-30 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tprobot', '0004_alter_deliver_order_deliver_order_processing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliver_order',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Deliver_product', to='tprobot.product'),
        ),
    ]
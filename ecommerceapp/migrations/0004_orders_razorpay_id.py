# Generated by Django 4.2.1 on 2024-01-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='razorpay_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
# Generated by Django 4.2.1 on 2023-10-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_orderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='price',
        ),
        migrations.AddField(
            model_name='stock',
            name='order_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='stock',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
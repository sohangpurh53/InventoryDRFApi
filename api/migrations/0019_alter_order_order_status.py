# Generated by Django 4.2.1 on 2023-09-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('successful', 'Successful'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
    ]

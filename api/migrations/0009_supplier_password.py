# Generated by Django 4.2.1 on 2023-09-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_stock_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
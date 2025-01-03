# Generated by Django 4.2.1 on 2023-09-17 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_supplier_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='email',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='password',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='supplier',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]

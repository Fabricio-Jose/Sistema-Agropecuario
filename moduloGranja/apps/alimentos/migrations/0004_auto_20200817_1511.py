# Generated by Django 3.0.9 on 2020-08-17 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0003_auto_20200817_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichaalimento',
            name='fecha_expiracion',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

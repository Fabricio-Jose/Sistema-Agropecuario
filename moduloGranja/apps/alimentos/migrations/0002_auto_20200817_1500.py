# Generated by Django 3.0.9 on 2020-08-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichaalimento',
            name='fecha_expiracion',
            field=models.DateField(default=8),
        ),
    ]
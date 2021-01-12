# Generated by Django 3.0.6 on 2020-08-17 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cluster', models.CharField(max_length=50)),
                ('capacidad', models.PositiveIntegerField(default=20)),
                ('nro_cerdos', models.PositiveIntegerField(default=0)),
                ('nro_galpon', models.PositiveIntegerField(default=0)),
                ('personal', models.ManyToManyField(to='personal.Personal')),
            ],
        ),
    ]

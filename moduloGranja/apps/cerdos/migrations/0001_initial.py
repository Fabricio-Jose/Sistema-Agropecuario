# Generated by Django 3.0.6 on 2020-08-17 02:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clusters', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cerdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cerdo', models.CharField(max_length=25)),
                ('raza', models.CharField(max_length=25)),
                ('fecha_nac', models.DateField(default=datetime.date.today)),
                ('peso', models.PositiveSmallIntegerField()),
                ('cluster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clusters.Cluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Engorde',
            fields=[
                ('cerdo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cerdos.Cerdo')),
                ('apto', models.BooleanField()),
                ('score', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nacido',
            fields=[
                ('cerdo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cerdos.Cerdo')),
                ('apto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reproductor',
            fields=[
                ('cerdo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cerdos.Cerdo')),
                ('nro_muestras', models.IntegerField()),
                ('nro_hijos', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reproductora',
            fields=[
                ('cerdo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cerdos.Cerdo')),
                ('nro_inseminaciones', models.PositiveIntegerField()),
                ('nro_partos', models.PositiveIntegerField()),
                ('fecha_gestacion', models.DateField(default=16)),
                ('embarazo', models.BooleanField(default=False)),
                ('riesgo', models.BooleanField(default=False)),
            ],
        ),
    ]

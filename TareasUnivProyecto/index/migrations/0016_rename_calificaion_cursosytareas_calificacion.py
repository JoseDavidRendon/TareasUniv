# Generated by Django 4.0.3 on 2022-06-25 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_cursosytareas_calificado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursosytareas',
            old_name='calificaion',
            new_name='calificacion',
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_alter_cursosytareas_anotacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursosytareas',
            name='calificaion',
            field=models.IntegerField(default=0),
        ),
    ]
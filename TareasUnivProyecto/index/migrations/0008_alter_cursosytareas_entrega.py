# Generated by Django 4.0.3 on 2022-06-17 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_alter_cursosytareas_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursosytareas',
            name='entrega',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

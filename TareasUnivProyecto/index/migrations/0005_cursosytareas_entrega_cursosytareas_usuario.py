# Generated by Django 4.0.3 on 2022-06-15 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_estadodelcurso_alter_cursosytareas_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursosytareas',
            name='entrega',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursosytareas',
            name='usuario',
            field=models.CharField(default='usuario', max_length=100),
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='formAgregarCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100)),
                ('tarea', models.CharField(max_length=100)),
                ('valor', models.IntegerField(max_length=500)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]

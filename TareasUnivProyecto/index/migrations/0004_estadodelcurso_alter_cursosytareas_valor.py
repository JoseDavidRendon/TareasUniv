# Generated by Django 4.0.3 on 2022-06-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_cursosytareas_delete_formagregarcurso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoDelCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100)),
                ('verificacion', models.CharField(default='pendiente', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='cursosytareas',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 3.0.2 on 2020-02-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200205_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='is_cell',
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(max_length=10),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_api_id', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
    ]

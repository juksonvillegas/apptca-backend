# Generated by Django 2.1 on 2019-02-26 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 2.1 on 2019-03-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='modelo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.1 on 2019-03-19 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0002_auto_20190317_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='extendido',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

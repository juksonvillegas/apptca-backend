# Generated by Django 2.1 on 2019-02-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=9)),
                ('dni', models.CharField(blank=True, max_length=8)),
                ('mayorista', models.BooleanField(default=False)),
                ('proveedor', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-19 13:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, srid=4326),
        ),
        migrations.AlterField(
            model_name='court',
            name='id',
            field=models.CharField(default=uuid.UUID('a6e6866f-3963-4fbf-a08f-935572c8c419'), max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
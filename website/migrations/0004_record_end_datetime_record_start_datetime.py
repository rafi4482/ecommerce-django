# Generated by Django 5.0.1 on 2024-01-25 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0003_rename_address_record_name_remove_record_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="end_datetime",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="record",
            name="start_datetime",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

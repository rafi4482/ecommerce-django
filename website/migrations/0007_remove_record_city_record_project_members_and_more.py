# Generated by Django 5.0.1 on 2024-01-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0006_remove_record_state_remove_record_zipcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="record",
            name="city",
        ),
        migrations.AddField(
            model_name="record",
            name="project_members",
            field=models.CharField(default="Enter project members", max_length=255),
        ),
        migrations.AddField(
            model_name="record",
            name="status",
            field=models.CharField(default="PRE", max_length=10),
        ),
    ]
from django.db import models
from django.utils import timezone

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=255, default='Default Intro Text')
    status = models.CharField(max_length=10, default='PRE')
    start_datetime = models.DateTimeField(default=timezone.now)
    end_datetime = models.DateTimeField(default=timezone.now)
    project_members = models.CharField(max_length=255, default='Enter project members')
    

    def __str__(self):
        return f"{self.name}"

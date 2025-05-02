from django.db import models
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    last_date_to_apply = models.DateTimeField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    eligibility = models.TextField(blank=True, null=True)
    apply_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

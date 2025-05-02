from django.core.management.base import BaseCommand
from jobs.models import Job
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Create dummy job data for testing'

    def handle(self, *args, **kwargs):
        Job.objects.all().delete()  # Clear existing jobs

        jobs = [
            {
                "title": "Assistant Professor",
                "description": "Looking for Assistant Professor in Computer Science.",
                "location": "New Delhi",
                "date_posted": timezone.now() - timedelta(days=5),
                "last_date_to_apply": timezone.now() + timedelta(days=25),
                "company_name": "University of Delhi",
                "job_type": "Full-time",
                "salary": "₹50,000 - ₹70,000",
                "eligibility": "PhD in relevant field.",
                "apply_link": "https://universityofdelhi.ac.in/jobs"
            },
            {
                "title": "Railway Ticket Collector",
                "description": "Recruitment for Ticket Collector in Indian Railways.",
                "location": "Mumbai",
                "date_posted": timezone.now() - timedelta(days=10),
                "last_date_to_apply": timezone.now() + timedelta(days=20),
                "company_name": "Indian Railways",
                "job_type": "Full-time",
                "salary": "₹25,000 - ₹35,000",
                "eligibility": "12th Pass",
                "apply_link": "https://indianrailways.gov.in/jobs"
            },
            {
                "title": "Bank PO",
                "description": "Probationary Officer recruitment in nationalized banks.",
                "location": "Chennai",
                "date_posted": timezone.now() - timedelta(days=3),
                "last_date_to_apply": timezone.now() + timedelta(days=30),
                "company_name": "State Bank of India",
                "job_type": "Full-time",
                "salary": "₹40,000 - ₹60,000",
                "eligibility": "Graduate in any discipline.",
                "apply_link": "https://sbi.co.in/careers"
            },
        ]

        for job_data in jobs:
            Job.objects.create(**job_data)

        self.stdout.write(self.style.SUCCESS('Dummy job data created successfully.'))

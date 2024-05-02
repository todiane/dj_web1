from django.db import models
from django.utils import timezone

class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="Company")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
    # class Meta:
    #     db_table = "custom_table_name"

class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


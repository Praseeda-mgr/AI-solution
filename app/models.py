from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SoftwareSolution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class PastSolution(models.Model):
    industry = models.CharField(max_length=200)
    description = models.TextField()

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    rating = models.IntegerField()  
    feedback = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

from django.db import models

class PhotoGallery(models.Model):
    event_name = models.CharField(max_length=200)  # Name of the event
    event_date = models.DateField()  # Date when the event occurred
    photo = models.ImageField(upload_to="event_photos/")  # Path to store uploaded photos
    description = models.TextField(blank=True, null=True)  # Description of the event or photo
    uploaded_by = models.CharField(max_length=100, blank=True, null=True)  # Name of the uploader
    upload_date = models.DateTimeField(auto_now_add=True)  # Timestamp of upload
    is_featured = models.BooleanField(default=False)  # Highlight the photo as featured
    location = models.CharField(max_length=255, blank=True, null=True)  # Location of the event
    is_public = models.BooleanField(default=True)  # Determines if the photo is publicly visible

    def __str__(self):
        return f"{self.event_name} ({self.event_date})"

class CustomerInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_details = models.TextField()
    inquiry_date = models.DateTimeField(auto_now_add=True)






from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class SoftwareSolution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class PastSolution(models.Model):
    industry = models.CharField(max_length=200)
    description = models.TextField()

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    rating = models.IntegerField()  # Out of 5
    feedback = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

class PhotoGallery(models.Model):
    event_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="event_photos/")
    event_date = models.DateField()

class CustomerInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_details = models.TextField()
    inquiry_date = models.DateTimeField(auto_now_add=True)

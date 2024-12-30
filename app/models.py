from django.db import models
from django.contrib.auth.models import User

class Solution(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()        
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)     
    image = models.ImageField(upload_to='solutions/', blank=True, null=True)  
    def __str__(self):
        return self.title


class PastSolution(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)  
    industry = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='past_solutions/', blank=True, null=True)
    def __str__(self):
        return self.title or "Untitled"

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=100, default='Anonymous') 
    published_date = models.DateField()


class Album(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='event_photos/', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)  
    image = models.ImageField(upload_to='album_photos/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Photo in {self.album.name if self.album else 'No Album'}"


class CustomerInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_details = models.TextField()
    message = models.TextField(blank=True, null=True)  # New field for additional messages
    def __str__(self):
        return f"{self.name} - {self.company_name}"


class Feedback(models.Model):
    name = models.CharField(max_length=100)  
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  
    message = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return f"{self.name} - {self.rating} Stars"


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
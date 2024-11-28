from django.urls import path
from app.views import *

urlpatterns = [
    path('navbar_footer/', navbar_footer, name='navbar_footer'),
    path("about_us/", about_us, name='about_us'),
    path("", home, name="home"),
    path('contact_us/', contact_us, name="contact_us"),
    path('thankyou/', thank_you, name="thank_you"),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    path('article/', article_list, name="article_list"),
     path('article/<int:id>/', article_detail, name="article_detail"),
]


from django.urls import path
from app.views import *

urlpatterns = [
    path('navbar_footer/', navbar_footer, name='navbar_footer'),
    path("", home, name="home"),
    path("contact-us/", contact_us, name="contact_us"),
    path("admin-area/", admin_area, name="admin_area"),
    path('thankyou/', thank_you, name='thank_you'),
    path('customer/', customer, name="customer"),
    path('inquiry/<int:id>/',view_inquiry, name="inquiry"),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    path('article/', article_list, name="article_list"),
     path('article/<int:id>/', article_detail, name="article_detail"),
]


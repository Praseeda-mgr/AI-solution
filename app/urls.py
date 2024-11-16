from django.urls import path
from app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("contact-us/", contact_us, name="contact_us"),
    path("admin-area/", admin_area, name="admin_area"),
    path('thankyou/', thank_you, name='thank_you'),
    path('customer/', CustomerInquiry, name="customer"),
]


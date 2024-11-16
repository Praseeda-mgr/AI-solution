from django import forms
from .models import CustomerInquiry

class CustomerInquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = ['name', 'email', 'phone_number', 'company_name', 'country', 'job_title', 'job_details']

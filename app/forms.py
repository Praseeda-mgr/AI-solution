from django import forms
from .models import CustomerInquiry, Feedback, Article

class CustomerInquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = ['name', 'email', 'phone_number', 'company_name', 'country', 'job_title', 'job_details']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['customer_name', 'rating', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'published_date']



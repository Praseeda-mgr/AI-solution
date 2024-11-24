from django import forms
from .models import CustomerInquiry, Feedbacks, Article

class CustomerInquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = ['name', 'email', 'phone_number', 'company_name', 'country', 'job_title', 'job_details']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['customer_name', 'rating', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'published_date', 'writer']  # Include all fields you want to manage
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input rounded-md shadow-sm',
                'placeholder': 'Enter the article title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md shadow-sm',
                'placeholder': 'Write the content here...',
                'rows': 10,
            }),
            'published_date': forms.DateInput(attrs={
                'class': 'form-input rounded-md shadow-sm',
                'type': 'date',
            }),
            'writer': forms.TextInput(attrs={
                'class': 'form-input rounded-md shadow-sm',
                'placeholder': 'Enter the writer\'s name',
            }),
        }



from django.contrib import admin
from .models import SoftwareSolution, PastSolution, Feedback, Article, CustomerInquiry

admin.site.register(SoftwareSolution)
admin.site.register(PastSolution)
admin.site.register(Feedback)
admin.site.register(Article)
admin.site.register(CustomerInquiry)

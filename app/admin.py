from django.contrib import admin
from django.utils.html import format_html
from .models import Solution, PastSolution, Article, CustomerInquiry, Feedback, Album, Photo

admin.site.register(Solution)
admin.site.register(PastSolution)
admin.site.register(Article)
admin.site.register(CustomerInquiry)
admin.site.register(Feedback)
admin.site.register(Album)
admin.site.register(Photo)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'published_date')
    search_fields = ('title', 'writer')

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)


class PastSolutionAdmin(admin.ModelAdmin):
    list_display = ('industry', 'description', 'image_preview')
    search_fields = ('industry', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 75px; height: auto;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'message', 'submitted_at') 
    search_fields = ('customer_name', 'message') 
    list_filter = ('rating',)  

class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company_name', 'job_title', 'country')
    search_fields = ('name', 'email', 'company_name', 'job_title')
from django.urls import path
from app.views import *

urlpatterns = [
    path('navbar_footer/', navbar_footer, name='navbar_footer'),
    path("about_us/", about_us, name='about_us'),
    path("", home, name="home"),
    path('contact_us/', contact_us, name="contact_us"),
    path('solutions/', solutions_list, name='solutions_list'),
        path('solutions/<int:id>/', solution_detail, name='solution_detail'),
    path('past-solutions/', past_solutions, name='past_solutions'),
        path('past-solution/<int:pk>/', past_solution_details, name='past_solution_details'),
    path('feedback/',feedback, name='feedback'),
        path('feedback/success/', lambda request: render(request, 'Feedback_success.html'), name='feedback_success'),
    path('article/', article_list, name="article_list"),
        path('article/<int:id>/', article_detail, name="article_detail"),
    path('albums/', album_list, name='album_list'),
        path('album/<int:album_id>/', album_detail, name='album_detail'), 
]


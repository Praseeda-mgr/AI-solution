from django.shortcuts import render, redirect, get_object_or_404
from .models import Solution,PastSolution, CustomerInquiry, Article, Feedback, Album, Event
from .forms import CustomerInquiryForm, FeedbackForm
from datetime import date
def navbar_footer(request):
    return render(request, 'navbar_footer.html')

def about_us(request):
    return render(request, "about_us.html")

def home(request):
    articles = Article.objects.all()[:4]
    solutions = Solution.objects.all()

    form = CustomerInquiryForm()
    feedbacks = Feedback.objects.all()[:4]
    return render(request, "home.html", {"solutions": solutions, "form": form, 'articles': articles,"feedbacks":feedbacks})


def contact_us(request):
    if request.method == "POST":
        form = CustomerInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thank_you.html")
    else:
        form = CustomerInquiryForm()
    return render(request, "contact_us.html", {"form": form})


def article_list(request):
    articles= Article.objects.all().order_by('-published_date')
    print(f"Found {articles.count()} articles.") 
    return render(request, 'articles.html', {'articles': articles})

    

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})


def solutions_list(request):
    solutions = Solution.objects.all().order_by('-created_at')
    return render(request, 'solutions.html', {'solutions': solutions})

def past_solutions(request):
    past_solutions = PastSolution.objects.all()
    return render(request, 'past_solutions.html', {'past_solutions': past_solutions})


def past_solution_details(request, pk):
    solution = get_object_or_404(PastSolution, pk=pk)
    return render(request, 'past_details.html', {'solution': solution})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')  
    else:
        form = FeedbackForm()
    feedback_list = Feedback.objects.all()  
    return render(request, 'feedback.html', {'form': form, 'feedback_list': feedback_list})


def solution_detail(request, id):
    solution = get_object_or_404(Solution, id=id)
    return render(request, 'solution_detail.html', {'solution': solution})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    photos = album.photos.all() 
    return render(request, 'album_detail.html', {'album': album, 'photos': photos})

def events(request):
    today = date.today()
    upcoming_events = Event.objects.filter(event_type='upcoming', date__gte=today).order_by('date')
    past_events = Event.objects.filter(event_type='past', date__lt=today).order_by('-date')
    return render(request, 'events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    })
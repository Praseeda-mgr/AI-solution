from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Solution,PastSolution, CustomerInquiry, Article, Feedback
from .forms import CustomerInquiryForm, FeedbackForm

def navbar_footer(request):
    return render(request, 'navbar_footer.html')

def about_us(request):
    return render(request, "about_us.html")

def home(request):
    articles = Article.objects.all()[:4]
    solutions = Solution.objects.all()
    form = CustomerInquiryForm()
    return render(request, "home.html", {"solutions": solutions, "form": form, 'articles': articles})


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
    solutions = PastSolution.objects.all()
    return render(request, 'past_solutions.html', {'solutions': solutions})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')  # Redirect after successful submission
    else:
        form = FeedbackForm()

    feedback_list = Feedback.objects.all().order_by('-created_at')  # Show all feedback (optional)
    return render(request, 'feedback.html', {'form': form, 'feedback_list': feedback_list})

def solution_detail(request, id):
    solution = get_object_or_404(Solution, id=id)
    return render(request, 'solution_detail.html', {'solution': solution})

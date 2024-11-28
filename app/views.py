from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import SoftwareSolution, CustomerInquiry, Article
from .forms import CustomerInquiryForm

def navbar_footer(request):
    return render(request, 'navbar_footer.html')

def about_us(request):
    return render(request, "about_us.html")

def home(request):
    articles = Article.objects.all()[:4]
    solutions = SoftwareSolution.objects.all()
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


def thank_you(request):
    return render(request, "thank_you.html")


def article_list(request):
    articles= Article.objects.all().order_by('-published_date')
    print(f"Found {articles.count()} articles.")  # Ensure this shows the correct number
    return render(request, 'articles.html', {'articles': articles})

    

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})


def submit_feedback(request):
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return redirect("home")
    return redirect("home")


def software_solution(request, solution_id):
    solution = SoftwareSolution.objects.get(id=solution_id)
    return render(request, "software_solution.html", {"solution": solution})


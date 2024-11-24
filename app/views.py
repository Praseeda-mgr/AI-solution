from django.shortcuts import render, redirect, get_object_or_404
from .models import SoftwareSolution, CustomerInquiry, Feedbacks, Article
from .forms import CustomerInquiryForm, FeedbackForm

def navbar_footer(request):
    return render(request, 'navbar_footer.html')

def about_us(request):
    return render(request, "about_us.html")

def home(request):
    articles = Article.objects.all()[:4]
    solutions = SoftwareSolution.objects.all()
    form = CustomerInquiryForm()
    feedback_form = FeedbackForm()
    return render(request, "home.html", {"solutions": solutions, "form": form, "feedback_form": feedback_form, 'articles': articles})

def contact_us(request):
    if request.method == "POST":
        form = CustomerInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = CustomerInquiryForm()
    return render(request, "contact_us.html", {"form": form})

def admin_area(request):
    if not request.user.is_authenticated:
        return redirect("admin:login")
    inquiries = CustomerInquiry.objects.all()
    return render(request, "admin_area.html", {"inquiries": inquiries})

def thank_you(request):
    return render(request, "thank_you.html")

def customer(request):
    return render(request, "customer.html")

def article_list(request):
    articles= Article.objects.all().order_by('-published_date')
    print(f"Found {articles.count()} articles.")  # Ensure this shows the correct number
    return render(request, 'articles.html', {'articles': articles})

    

def article_detail(request, id):
    # Fetch the article by its ID, or return a 404 error if not found
    article = get_object_or_404(Article, id=id)
    # Render the article_detail template with the article context
    return render(request, 'article_detail.html', {'article': article})


def submit_feedback(request):
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return redirect("home")
    return redirect("home")

# View_inquiry details 
def view_inquiry(request, id):
    inquiry = get_object_or_404(CustomerInquiry, id=id)
    return render(request, "view_inquiry.html", {"inquiry": inquiry})


def software_solution(request, solution_id):
    solution = SoftwareSolution.objects.get(id=solution_id)
    return render(request, "software_solution.html", {"solution": solution})


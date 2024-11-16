from django.shortcuts import render, redirect, get_object_or_404
from .models import SoftwareSolution, CustomerInquiry, Feedback
from .forms import CustomerInquiryForm, FeedbackForm

def home(request):
    solutions = SoftwareSolution.objects.all()
    form = CustomerInquiryForm()
    feedback_form = FeedbackForm()
    return render(request, "home.html", {"solutions": solutions, "form": form, "feedback_form": feedback_form})

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

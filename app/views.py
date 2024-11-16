from django.shortcuts import render, redirect
from .models import SoftwareSolution, CustomerInquiry
from .forms import CustomerInquiryForm

def home(request):
    solutions = SoftwareSolution.objects.all()
    return render(request, "home.html", {"solutions": solutions})

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


# View_inquiry details 
from django.shortcuts import render, get_object_or_404
from .models import CustomerInquiry
def view_inquiry(request, id):
    inquiry = get_object_or_404(CustomerInquiry, id=id)
    return render(request, "view_inquiry.html", {"inquiry": inquiry})


def software_solution(request, solution_id):
    solution = SoftwareSolution.objects.get(id=solution_id)
    return render(request, "software_solution.html", {"solution": solution})

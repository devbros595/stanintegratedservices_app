from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


# Create your views here.


def index_view(request):
    return render(request, "stanintegratedservices_app/index.html")


def about_view(request):
    return render(request, "stanintegratedservices_app/about.html")


def services_view(request):
    return render(request, "stanintegratedservices_app/services.html")


def why_choose_us_view(request):
    return render(request, "stanintegratedservices_app/why_choose_us.html")



def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        service = request.POST.get("service")
        message = request.POST.get("message")

        if not all([name, phone, address, service]):
            return JsonResponse(
                {"status": "error", "message": "Please fill in all required fields."},
                status=400,
            )

        ContactMessage.objects.create(
            name=name,
            phone=phone,
            address=address,
            service=service,
            message=message,
        )

        return JsonResponse(
            {
                "status": "success",
                "message": "Thank you! Your message has been sent successfully.",
            }
        )

    return render(request, "stanintegratedservices_app/contact.html")

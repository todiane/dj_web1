from django.shortcuts import render

from app.models import (
    GeneralInfo,
    Service,
    Testimonial,
    FrequentlyAskedQuestion,
)


def index(request):

    general_info = GeneralInfo.objects.first() # None

    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()

    default_value = ""

    context = {
        "company_name": getattr(general_info, "company_name", default_value),
        "location": getattr(general_info, "location", default_value),
        "email": getattr(general_info, "email", default_value),
        "phone": getattr(general_info, "phone", default_value),
        "open_hours": getattr(general_info, "open_hours", default_value),
        "video_url": getattr(general_info, "video_url", default_value),
        "twitter_url": getattr(general_info, "twitter_url", default_value),
        "github_url": getattr(general_info, 
        "github_url", default_value),
        "linkedin_url": getattr(general_info, "linkedin_url", default_value),

        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
    }

    return render(request, "index.html", context)


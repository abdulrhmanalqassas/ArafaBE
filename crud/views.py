from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Testimonials


def index(request):
    latest_testimonials_list = Testimonials.objects.order_by("-testimonials_date")[:5]

    data = [
        {
            "id": q.id,
            "text": q.testimonials_text,
            "name": q.testimonials_name,
            "job": q.testimonials_job,
            "date": q.testimonials_date,
            "stars": q.stars,
            "image_url": q.image.url if q.image else None ,
        }
        for q in latest_testimonials_list
    ]

    return JsonResponse(data, safe=False)


# Leave the rest of the views (detail, results, vote) unchanged
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import backGroundImages


def index(request):
    latest_testimonials_list = backGroundImages.objects.all()
    data = [
        {
            "image_url": q.image.url if q.image else None ,
        }
        for q in latest_testimonials_list
    ]

    return JsonResponse(data, safe=False)


# Leave the rest of the views (detail, results, vote) unchanged
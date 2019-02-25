from django.shortcuts import render
from .models import Card

# Create your views here.

def home(request):
    queryset = Card.objects.all()
    context = {
        "object_list":queryset,
    }
    return render(request,'main/home.html', context)

def timeline(request):
    return render(request,'main/timeline.html', {})

def faq(request):
    return render(request,'main/FAQ.html', {})

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'csite/index.html')

def contact(request):
    return render(request, 'csite/contact.html')

def elements(request):
    return render(request, 'csite/elements.html')

def blog(request):
    return render(request, 'csite/blog.html')

def speakers(request):
    return render(request, 'csite/speakers.html')

def tickets(request):
    return render(request, 'csite/tickets.html')

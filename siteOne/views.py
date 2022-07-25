from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('Hi There. This is About Page!')

def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Hi There. This is Home Page!'')

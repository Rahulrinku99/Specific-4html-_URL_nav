from django.shortcuts import render

# Create your views here.

def sanju(request):
    return render(request,'sanju.html')

def boult(request):
    return render(request,'boult.html')
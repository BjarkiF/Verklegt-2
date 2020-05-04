from django.shortcuts import render

def index(request):
    return render(request, 'items/index.html')

def all(request):
    return render(request, 'items/all.html')
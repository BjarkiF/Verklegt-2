from django.shortcuts import render

def index(request):
    # TODO: add data from the manage config here.
    return render(request, 'about/index.html')

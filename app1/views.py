from django.shortcuts import render

# Create your views here.

# index page
def index(request):
    return render(request, "app1/index.html")
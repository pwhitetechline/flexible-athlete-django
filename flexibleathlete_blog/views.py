from django.shortcuts import render
from markdownx.utils import markdownify
from django.shortcuts import get_object_or_404

# Homepage view
def home(request):
    return render(request, 'home/home.html')

# About Sub-Page Views
def stories(request):
    return render(request, 'about/stories.html')

def nutrition(request):
    return render(request, 'about/nutrition.html')

# Products Page View
def products(request):
    return render(request, 'products/products.html')

# Contact Page View
def contact(request):
    return render(request, 'contact/contact.html')

# Videos Sub-Page Views
def tinnitus(request):
    return render(request, 'videos/tinnitus.html')

def interviews(request):
    return render(request, 'videos/interviews.html')
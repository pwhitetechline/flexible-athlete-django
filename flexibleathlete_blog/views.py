from django.shortcuts import render
from markdownx.utils import markdownify
from django.shortcuts import get_object_or_404

# Homepage view
def home(request):
    return render(request, 'home/home.html')

# About Sub-Page Views
def success_stories(request):
    return render(request, 'about/success_stories.html')

def sports_nutrition(request):
    return render(request, 'about/sports_nutrition.html')

def julie_donnelly(request):
    return render(request, 'about/julie_donnelly.html')

def flexible_athlete_treatment(request):
    return render(request, 'about/flexible_athlete_treatment.html')

def focused_flexibilty_training(request):
    return render(request, 'about/focused_flexibilty_training.html')

def wny_muscles_cause_pain(request):
    return render(request, 'about/wny_muscles_cause_pain.html')

def muscle_knots_cause_joint_pains(request):
    return render(request, 'about/muscle_knots_cause_joint_pains.html')

def how_this_system_works_to_relieve_knots(request):
    return render(request, 'about/how_this_system_works_to_relieve_knots.html')

def therapy_appointment(request):
    return render(request, 'about/therapy_appointment.html')

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
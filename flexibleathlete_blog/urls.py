
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('about/julie_donnelly/', views.julie_donnelly, name='julie_donnelly'),
    path('about/sports_nutrition/', views.sports_nutrition, name='sports_nutrition'),
    path('about/success_stories/', views.success_stories, name='success_stories'),
    path('about/flexible_athlete_treatment/', views.flexible_athlete_treatment, name='flexible_athlete_treatment'),
    path('about/focused_flexibilty_training/', views.focused_flexibilty_training, name='focused_flexibilty_training'),
    path('about/wny_muscles_cause_pain/', views.wny_muscles_cause_pain, name='wny_muscles_cause_pain'),
    path('about/muscle_knots_cause_joint_pains/', views.muscle_knots_cause_joint_pains, name='muscle_knots_cause_joint_pains'),
    path('about/how_this_system_works_to_relieve_knots/', views.how_this_system_works_to_relieve_knots, name='how_this_system_works_to_relieve_knots'),
    path('about/therapy_appointment/', views.therapy_appointment, name='therapy_appointment'),
    path('products/',views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    # For videos, you might include another app or define them here
    path('videos/tinnitus/', views.tinnitus, name='tinnitus'),
    path('videos/interviews/', views.interviews, name='interviews'),
    # Add other paths as needed
]


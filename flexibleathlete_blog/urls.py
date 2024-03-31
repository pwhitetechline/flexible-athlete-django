
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('about/nutrition/', views.nutrition, name='nutrition'),
    path('about/stories/', views.stories, name='stories'),
    path('products/',views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    # For videos, you might include another app or define them here
    path('videos/tinnitus/', views.tinnitus, name='tinnitus'),
    path('videos/interviews/', views.interviews, name='interviews'),
    # Add other paths as needed
]


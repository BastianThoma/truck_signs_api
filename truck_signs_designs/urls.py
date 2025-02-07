"""truck_signs_designs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Uses 'path' (recommended method in Django 2.x+)
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render

# Added a custom view for the home page that returns a simple message
def home_view(request):
    return HttpResponse("Welcome to the Truck Signs API")

urlpatterns = [
    path('admin/', admin.site.urls),  # Standard admin route
    path("", home_view, name="home"),  # This path is a custom home page view
    # path('', HomePageAPI, name='home'), 
    path('truck-signs/', include('backend.urls', namespace='trucks-signs-namespace')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

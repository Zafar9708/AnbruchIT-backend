# urls.py

from django.urls import path
from .views import ContactView, ContactViews

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),  # Handles the form submission
    path('contactus/', ContactViews.as_view(), name='contactus'),  # Optionally for a different view
]

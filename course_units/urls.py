from django.urls import path
from . import views

urlpatterns = [
    # Empty string "" because the base URL is already handled by PluginURLs.REGEX in apps.py
    path("", views.units_view, name="units_view"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("units/", views.units_view, name="units_view"),
]

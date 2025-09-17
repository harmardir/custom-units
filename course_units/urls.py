from django.urls import path, re_path
from . import views

urlpatterns = [
    # Capture course_id in the URL
    re_path(r'^courses/(?P<course_id>[^/]+)/units/$', views.units_view, name='units_view'),
]

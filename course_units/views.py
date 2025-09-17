from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from xmodule.modulestore.django import modulestore
from opaque_keys.edx.keys import CourseKey

@login_required
def units_view(request, course_id):
    """
    Display a grid of vertical units for the given course.
    """
    store = modulestore()
    course_key = CourseKey.from_string(course_id)
    
    # Collect all vertical units
    units = [
        {"id": str(block.location), "title": getattr(block, 'display_name', 'No Name')}
        for block in store.get_items(course_key)
        if block.location.category == 'vertical'
    ]
    
    context = {
        "course_id": course_id,
        "units": units,
    }
    return render(request, "course_units/units.html", context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def units_view(request, course_id):
    """
    Display a grid of units for the given course.
    For now, we use dummy units. Later replace with Course Blocks API calls.
    """
    # Example dummy data
    units = [
        {"id": f"{course_id}+type@vertical+block@unit1", "title": "Unit 1"},
        {"id": f"{course_id}+type@vertical+block@unit2", "title": "Unit 2"},
        {"id": f"{course_id}+type@vertical+block@unit3", "title": "Unit 3"},
    ]

    context = {
        "course_id": course_id,
        "units": units,
    }
    return render(request, "course_units/units.html", context)

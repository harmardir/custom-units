from setuptools import setup, find_packages

setup(
    name="course-units",
    version="0.1.0",
    description="Custom Django app to display course units as a grid.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "lms.djangoapp": [
            "course_units = course_units.apps:CourseUnitsConfig",
        ],
    },
)

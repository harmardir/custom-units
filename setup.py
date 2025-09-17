# pylint: disable=open-builtin
from __future__ import absolute_import, print_function, unicode_literals

import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split("#")[0].strip() for line in open(path).readlines() if is_requirement(line.strip())
        )
    return list(requirements)

def is_requirement(line):
    return not (
        line == ""
        or line.startswith("-c")
        or line.startswith("-r")
        or line.startswith("#")
        or line.startswith("-e")
        or line.startswith("git+")
    )

# Optional: if you want to include README or CHANGELOG
README = open(os.path.join(os.path.dirname(__file__), "README.md")).read() if os.path.exists("README.md") else ""
CHANGELOG = open(os.path.join(os.path.dirname(__file__), "CHANGELOG.rst")).read() if os.path.exists("CHANGELOG.rst") else ""

setup(
    name="course-units",
    version="0.1.0",
    packages=find_packages(),
    package_data={"": ["*.html"]},  # include Mako templates
    include_package_data=True,
    license="Proprietary",
    description="Custom Django app to display course units as a grid.",
    long_description=README + "\n\n" + CHANGELOG,
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/your-org/custom-units",
    install_requires=load_requirements("requirements/common.in") if os.path.exists("requirements/common.in") else [],
    zip_safe=False,
    keywords="Django, Open edX, course units",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "lms.djangoapp": [
            "course_units = course_units.apps:CourseUnitsConfig",
        ],
        "cms.djangoapp": [
            "course_units = course_units.apps:CourseUnitsConfig",
        ],
    },
)

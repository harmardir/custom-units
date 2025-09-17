from django.apps import AppConfig

from edx_django_utils.plugins import PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType

class CourseUnitsConfig(AppConfig):
    name = "course_units"
    label = "course_units"
    verbose_name = "Course Units"

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                # Regex to mount your URLs under course_id
                PluginURLs.REGEX: r"^courses/(?P<course_id>[^/]+)/units/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        }
    }

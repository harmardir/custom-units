from edx_django_utils.plugins import PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType

plugin_app = {
    PluginURLs.CONFIG: {
        ProjectType.LMS: {
            PluginURLs.NAMESPACE: "course_units",
            PluginURLs.REGEX: r"^courses/(?P<course_id>[^/]+)/units/",
            PluginURLs.RELATIVE_PATH: "urls",
        }
    }
}

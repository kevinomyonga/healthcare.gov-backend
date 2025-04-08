import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "healthcare_gov_swe6160.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import healthcare_gov_swe6160.users.signals  # noqa: F401

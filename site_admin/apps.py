from django.apps import AppConfig


class SiteAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_admin'
    verbose_name = 'Gestão do Site'

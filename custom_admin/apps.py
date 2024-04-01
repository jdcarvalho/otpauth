from django.apps import AppConfig


from django.contrib.admin.apps import AdminConfig as BaseAdminConfig


class CustomAdminSettings(BaseAdminConfig):
    default_site = "custom_admin.sites.CustomAdminSite"
    app_label = "custom_admin"


class CustomAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_admin'
    app_label = 'admin'

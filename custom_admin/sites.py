from django.contrib import admin
from django.urls import path, reverse_lazy as _

from custom_admin.models import UserOTPData
from custom_admin.views import AdminSetup2faView, AdminValidateOTPView
from django.contrib.auth import REDIRECT_FIELD_NAME

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        base_urlpatterns = super().get_urls()

        extra_urlpatterns = [
            path("setup-two-factor/",
                 self.admin_view(AdminSetup2faView.as_view()),
                 name="setup-2fa"
            ),
            path(
                "validate-otp/",
                self.admin_view(AdminValidateOTPView.as_view()),
                name="validate-2fa"
            ),
        ]

        return extra_urlpatterns + base_urlpatterns

    def login(self, request, *args, **kwargs):
        if request.method != 'POST':
            return super().login(request, *args, **kwargs)

        username = request.POST.get('username')
        two_factor_data = UserOTPData.objects.filter(
            user__username=username
        ).first()

        request.POST._mutable = True
        if two_factor_data:
            request.POST[REDIRECT_FIELD_NAME] = _('admin:validate-2fa')

        request.POST._mutable = False

        return super().login(request, *args, **kwargs)

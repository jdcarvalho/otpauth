from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import UserOTPData
from .service import OTPService
from django import forms


class AdminSetup2faView(TemplateView):
    context = {}
    template_name = "2fa/setup.html"

    def post(self, request):
        user = request.user
        try:
            service = OTPService()
            otp_data = UserOTPData.upsert_opt_data(user)
            qr_code = service.generate_auth_qrcode()
            self.context["otp_secret"] = service.secret_key
            self.context["qr_code"] = qr_code
            otp_data.otp_secret = service.secret_key
            otp_data.save()
        except ValidationError as exc:
            self.context["form_errors"] = exc.messages

        return self.render_to_response(self.context)


class AdminValidateOTPView(FormView):
    template_name = "2fa/validate.html"
    success_url = reverse_lazy("admin:index")

    class Form(forms.Form):
        otp = forms.CharField(required=True)

        def clean_otp(self):
            if not self.user.otpdata:
                raise ValidationError(
                    "Oops! Two-factor authentication isn't set up")

            otp = self.cleaned_data.get('otp')
            service = OTPService(self.user.otpdata.first().otp_secret)
            if not service.validate_otp(otp):
                raise ValidationError('Invalid code, please try again.')
            return otp

    def get_form_class(self):
        return self.Form

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.user = self.request.user
        return form

    def form_valid(self, form):
        return super().form_valid(form)

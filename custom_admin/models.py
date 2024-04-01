from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class UserOTPData(models.Model):

    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='otpdata', null=False, blank=False,
    )

    otp_secret = models.CharField(
        max_length=255, null=True, blank=True, default=''
    )

    @staticmethod
    def upsert_opt_data(user):
        try:
            otp_data = UserOTPData.objects.filter(user=user)[:1].get()
            return otp_data
        except UserOTPData.DoesNotExist:
            otp_data = UserOTPData(user=user)
            otp_data.save()
            return otp_data

    class Meta:
        db_table = 'user_otp_data'

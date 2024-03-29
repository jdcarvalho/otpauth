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

    class Meta:
        db_table = 'user_otp_data'

from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class UserOTPData(models.Model):

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name=''
    )

    class Meta:
        db_table = 'user_otp_data'

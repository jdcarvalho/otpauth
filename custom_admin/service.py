
class OTPService(object):

    secret_key = ''

    def __init__(self, secret_key=None):
        self.secret_key = secret_key

    def generate_auth_qrcode(self):
        """
        This method will generate the two-factor otp secret key for the
        current user and the QR code image for the autentication App
        :return: The SVG image for QR code painting
        """
        import pyotp
        import qrcode.image.svg
        self.secret_key = pyotp.random_base32()
        totp = pyotp.TOTP(self.secret_key)
        qr_uri = totp.provisioning_uri(
            name='My fabulous application',
            issuer_name='My fabulous application'
        )
        image_factory = qrcode.image.svg.SvgPathImage
        qr_code_image = qrcode.make(
            qr_uri,
            image_factory=image_factory
        )
        return qr_code_image.to_string().decode('utf_8')

    def validate_otp(self, otp_code):
        """
        This method will validate the otp code for the current secret_key
        :param otp_code:
        :return: Boolean
        """
        import pyotp
        totp = pyotp.TOTP(self.secret_key)
        return totp.verify(otp_code)

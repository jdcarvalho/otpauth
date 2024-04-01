### Two-Factor Authentication with OTP Repository

This repository provides a comprehensive implementation in Django of two-factor 
authentication (2FA) using one-time passwords (OTP). 
The goal of this project is to be a proof of concept to enhance the 
security of user authentication by adding an additional 
layer of verification beyond traditional 
username/password combinations.

Overall, this repository serves as a robust solution for implementing 
two-factor authentication with OTPs in Django, enhancing the security posture
of applications and protecting user accounts from unauthorized access.

The diagram below shows the typical OTP flow.

![Image](https://raw.githubusercontent.com/jdcarvalho/otpauth/master/custom_admin/static/img/otp-flow.png)

### Steps to test this POC
1. Make migrations, Migrate and create a superuser:

```shell
./manage.py makemigrations
```
```shell
./manage.py migrate
```
```shell
./manage.py createsuperuser
```

2. Run the application and login

```shell
./manage.py runserver
```

3. Activate two-factor authentication at admin dashboard

4. Logout then log in again

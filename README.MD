
### Two-Factor Authentication with OTP Repository
#### https://joaodecarvalho.com/python/django/2fa/2025/06/25/poc-django-2fa-implementation/#/

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
1. Create a new enviroment for the project, update base package and install 
the requirements.txt file content
```shell
python3.x -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel
pip install -r requirements.txt
```

2. Make migrations, Migrate and create a superuser:

```shell
./manage.py makemigrations
```
```shell
./manage.py migrate
```
```shell
./manage.py createsuperuser
```

3. Run the application and login

```shell
./manage.py runserver
```

4. Activate two-factor authentication at admin dashboard

5. Logout then log in again

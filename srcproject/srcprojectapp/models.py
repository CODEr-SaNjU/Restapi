from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.utils import timezone, tree
from django.core.validators import RegexValidator

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        "Email Address",
        max_length=255,
        unique=True,
        error_messages={'unique': ("A user with that Email address already exists")})

    phone_regex = RegexValidator(regex=r"^(?:[0-9]●?){6,14}[0-9]$", message=(
        "Enter a valid international mobile phone number "))

    mob_number = models.CharField(
        "Phone Number ",
        validators=[phone_regex],
        max_length=20,
        unique=True,
        error_messages={'unique': (
            "A user with that phone number address already exists")},
        )
    first_name = models.CharField("First Name", max_length=300)
    last_name = models.CharField('Last Name',max_length=300)
    user_type = models.CharField('User Type',max_length=300)

    is_active = models.BooleanField(default=True)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)  # a superuser
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mob_number']

    class Meta:
        ordering = ['email']
        verbose_name = ('User Profile')
        verbose_name_plural = ('Users Profile')

    #if we want send a mail to user when user is create 
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        send email to this user
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class EmailOtp(models.Model):
    email = models.EmailField(max_length=254,unique=True)
    otp = models.CharField(max_length=8,blank=True,null=True)
    count       = models.IntegerField(default = 0, help_text = 'Number of otp sent')
    logged      = models.BooleanField(default = False, help_text = 'If otp verification got successful')
    forgot      = models.BooleanField(default = False, help_text = 'only true for forgot password')
    forgot_logged = models.BooleanField(default = False, help_text = 'Only true if validdate otp forgot get successful')

    def __str__(self):
        return str(self.email) + 'is sent' + str(self.otp)


class LeadGenerator(models.Model):
    lead_name       = models.CharField(max_length=200)
    lead_source     = models.CharField(max_length=300)
    lead_user_email = models.EmailField(max_length=300)
    lead_created_at = models.DateTimeField('lead created', default=timezone.now)

    
    def __str__(self):
        return self.lead_name
        
    class Meta:
        verbose_name = ('Lead Generator')
        verbose_name_plural = ('Lead Generators')
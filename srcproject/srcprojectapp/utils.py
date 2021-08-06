import random
from django.core.mail import send_mail

def send_mail_func(subject,message,from_email,to_email):
    send_mail(subject,message,from_email,to_email)

def otp_generator():
    otp = random.randint(9999,999999)
    return otp
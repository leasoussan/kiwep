from django.conf import settings 
from django.core.mail import send_mail 



def send_welcome_signup(user):
    subject = f'welcome {user}to KIWEP '
    message = f'Hi {user}, thank you for registering To KIWEP.'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [user.email,] 
    print(recipient_list)
    send_mail(subject, message, email_from, recipient_list, fail_silently = False ) 



def send_message(user, subject, text):
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [user.email, ] 
    send_mail( subject, text, email_from, recipient_list,fail_silently = False ) 
    

def XXX(message):
    subject = f'Your Message to {message.email} was sent'
    text = f'Hi, thank you for your interest we will get back to you shortly'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [message.email, ] 
    send_mail(subject, text, email_from, recipient_list ,fail_silently = False) 
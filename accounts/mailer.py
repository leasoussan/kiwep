from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

def send_welcome_signup(user):
    wlcm_msg= _('welcome')
    kiwep = _('to KIWEP')
    subject = f' {wlcm_msg} {user} {kiwep} '
    message = _('registration_email_subject')
    translation.activate(user.language_code)
    html_message = render_to_string('emails/welcome.html', {'user':user})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message,  email_from, recipient_list, fail_silently=False, html_message=html_message )


def institution_welcome_email(user):
    wlcm_msg= _('welcome')
    kiwep = _('to KIWEP')
    subject = f' {wlcm_msg} {user} {kiwep} '
    message = _('registration_email_subject')
    translation.activate(user.language_code)
    html_message = render_to_string('emails/institution_welcome.html', {'user':user})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message,  email_from, recipient_list, fail_silently=False, html_message=html_message )




def send_institution_signup_invite(institution_invite):
    wlcm_msg = _('institution_invitation_ registration')
    kiwep = _('to_kiwep')
    subject = f' {wlcm_msg} {institution_invite.email} {kiwep} '
    message = _('registration_invitation_email_subject')
    # translation.activate(email.language_code)
    html_message = render_to_string('emails/institution_email_invite.html', {'institution_invite': institution_invite})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [institution_invite.email, ]
    # print('institution-invite' + f'{institution_invite.key}')

    send_mail(subject, message, email_from, recipient_list, fail_silently=False, html_message=html_message)


def send_speaker_signup_invit(speaker_invite):
    wlcm_msg = _('speaker_invitation_registration')
    kiwep = _('to_kiwep')
    subject = f' {wlcm_msg} {kiwep} '
    message = _('registration_invitation_email_subject')
    # translation.activate(email.language_code)
    html_message = render_to_string('emails/speaker_invite.html', {'speaker_invite': speaker_invite})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [speaker_invite.email ]
    # print(reverse_lazy('register') + f'key={speaker_invite.key}')
    send_mail(subject, message, email_from, recipient_list, fail_silently=False, html_message=html_message)


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


def new_team_member(user):
    subject = f'Welcome to the '
    text = f'Welcome to team  ! good luck on your project '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail(subject, text, email_from, recipient_list, fail_silently=False)

# Fail_silently = True when deployed 
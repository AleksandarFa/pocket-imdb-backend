from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from requests.exceptions import RequestException


@shared_task(name='SendEmailTask', autoretry_for=(RequestException, ))
def send_email_task(subject, to, default_from, email_html_message):
    msg = EmailMultiAlternatives(
        subject,
        email_html_message,
        default_from,
        to,
        alternatives=((email_html_message, 'text/html'), ),
    )
    msg.send()

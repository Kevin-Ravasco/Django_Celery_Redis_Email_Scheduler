from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Subscriber


@shared_task
def send_monthly_emails():
    subscribers = Subscriber.objects.filter(is_subscribed=True)
    for subscriber in subscribers:
        context = {'subscriber': subscriber}
        message = render_to_string('subscriptions/email.html', context)
        send_mail('x-Journal Subscription', message, 'me@gmail.com', [subscriber])
        sleep(2)
    return None


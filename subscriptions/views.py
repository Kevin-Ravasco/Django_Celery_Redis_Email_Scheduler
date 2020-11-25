from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView

from .forms import SubscribeForm
from .models import Subscriber
from .tasks import send_monthly_emails


def home(request):
    subscribers = Subscriber.objects.all().order_by('-timestamp')
    send_monthly_emails.delay()  # use celery to send emails
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed')
            return redirect(reverse('home'))
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, str(field.label) + ' : ' + str(error))
    context = {'form': form, 'subscribers': subscribers}
    return render(request, 'subscriptions/index.html', context)



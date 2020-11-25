from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_filter = ['is_subscribed']
    list_display = ['email', 'is_subscribed', 'timestamp']
    search_fields = ['email', 'timestamp']


admin.site.register(Subscriber, SubscriberAdmin)
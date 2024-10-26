from django.contrib import admin
from apps.notification.models import Notification
# Register your models here.
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'created_at']
    list_filter = ['user', 'message', 'created_at']
    search_fields = ['user', 'message', 'created_at']
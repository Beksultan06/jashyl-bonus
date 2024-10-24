from django.contrib import admin
from apps.base.models import Partners
# Register your models here.
@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']

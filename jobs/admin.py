from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'date_posted', 'last_date_to_apply')
    search_fields = ('title', 'company_name', 'location')
    list_filter = ('date_posted', 'last_date_to_apply')

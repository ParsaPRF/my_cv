from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # This ensures that you can see your fields in the admin panel
    list_display = ('full_name', 'job_title', 'email')


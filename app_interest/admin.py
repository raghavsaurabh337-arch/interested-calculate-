from django.contrib import admin
from app_interest.models import SimpleInterest


class SimpleInterestAdmin(admin.ModelAdmin):
    list_display = ('principal', 'rate', 'time')


admin.site.register(SimpleInterest, SimpleInterestAdmin)
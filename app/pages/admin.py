from django.contrib import admin
from .models import Card, MenuItem, ProgressItem, AdditionalInfo

# Register your models here.
admin.site.register(Card)
admin.site.register(MenuItem)
admin.site.register(ProgressItem)
admin.site.register(AdditionalInfo)

from django.contrib import admin
from .models import NightEvent, DayEvent, UploadFile

class EventAdmin(admin.ModelAdmin):
    search_fields = ['group', 'editor']

# Register your models here.
admin.site.register(NightEvent, EventAdmin)
admin.site.register(DayEvent, EventAdmin)
admin.site.register(UploadFile)
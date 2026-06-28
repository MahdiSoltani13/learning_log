from django.contrib import admin

# Register your models here.
from .models import Topic, Entry
admin.site.register(Topic)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'short_entry', 'date_added')

admin.site.register(Entry, EntryAdmin)
from django.contrib import admin
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date',)

admin.site.register(Note, NoteAdmin)
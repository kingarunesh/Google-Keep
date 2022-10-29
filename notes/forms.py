from django import forms
from django.forms import ModelForm, widgets
from notes.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        # fields = "__all__"
        fields = ["title","note","category"]
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "note": forms.Textarea(attrs={'class':'form-control'}),
            "category": forms.Select(attrs={'class':'form-control'}),
        }
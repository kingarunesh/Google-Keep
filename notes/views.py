from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView
from notes.models import Note
from django.urls import path
from django.urls import reverse_lazy
from notes.forms import NoteForm


class DashboardTemplateView(TemplateView):
    template_name = "notes/dashboard.html"
    print(path)


class NoteListView(ListView):
    model = Note
    context_object_name = "notes_list"
    print(path)


class CreateNoteView(CreateView):
    model = Note
    # fields = ["title", "note", "category"]
    form_class = NoteForm
    success_url = reverse_lazy("notes:notes_list")


class NoteDetailView(DetailView):
    model = Note


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("notes:notes_list")


class NoteUpdateView(UpdateView):
    model = Note
    fields = ["title", "note", "done", "category"]
    success_url = reverse_lazy("notes:notes_list")


class DoneNoteView(ListView):
    model = Note
    queryset = Note.objects.filter(done=True).all()
    context_object_name = "done_notes"
    template_name = "notes/done-notes.html"


class PendingNoteView(ListView):
    model = Note
    queryset = Note.objects.filter(done=False).all()
    context_object_name = "pending_notes"
    template_name = "notes/pending-notes.html"
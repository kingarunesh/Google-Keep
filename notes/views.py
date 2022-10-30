from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView
from notes.models import Note
from django.urls import path
from django.urls import reverse_lazy
from notes.forms import NoteForm, UpdateNoteForm


class DashboardTemplateView(TemplateView):
    template_name = "notes/dashboard.html"


class NoteListView(ListView):
    model = Note
    queryset = Note.objects.filter(trash=False).order_by("-updated_date").all()
    context_object_name = "notes_list"


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


class MoveNoteToTrashView(UpdateView):
    model = Note
    fields = ["trash"]
    template_name = "notes/move_note_trash.html"
    success_url = reverse_lazy("notes:notes_list")


class TrashNoteView(ListView):
    model = Note
    queryset = Note.objects.filter(trash=True).order_by("id").all()
    context_object_name = "trash_notes_list"
    template_name = "notes/trash_notes_list.html"


class NoteUpdateView(UpdateView):
    model = Note
    # fields = ["title", "note", "done", "category"]
    form_class = UpdateNoteForm
    success_url = reverse_lazy("notes:notes_list")


class DoneNoteView(ListView):
    model = Note
    queryset = Note.objects.filter(done=True).filter(trash=False).all()
    context_object_name = "done_notes"
    template_name = "notes/done-notes.html"


class PendingNoteView(ListView):
    model = Note
    queryset = Note.objects.filter(done=False).filter(trash=False).all()
    context_object_name = "pending_notes"
    template_name = "notes/pending-notes.html"
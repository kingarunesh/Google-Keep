from django.urls import path
from . import views


app_name = "notes"

urlpatterns = [
    path("", view=views.DashboardTemplateView.as_view(), name="dashboard"),
    path("notes/", view=views.NoteListView.as_view(), name="notes_list"),
    path("add/", view=views.CreateNoteView.as_view(), name="create_note"),
    path("note-detail/<int:pk>", view=views.NoteDetailView.as_view(), name="notes-detail"),
    path("move-note-trash/<int:pk>", view=views.MoveNoteToTrashView.as_view(), name="move-note-trash"),
    path("trash-note-view/", view=views.TrashNoteView.as_view(), name="trash-note-view"),
    path("delete-note/<int:pk>", view=views.NoteDeleteView.as_view(), name="delete-note"),
    path("update-note/<int:pk>", view=views.NoteUpdateView.as_view(), name="update-note"),
    path("done-notes/", view=views.DoneNoteView.as_view(), name="done_notes"),
    path("pending-note/", view=views.PendingNoteView.as_view(), name="pending_notes")
]
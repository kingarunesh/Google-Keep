from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    deadline = models.DateTimeField(blank=True, null=True)
    trash = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    CAT_LIST = [
        ('Grocery','Grocery'),
        ('Travel','Travel'),
        ('Sports','Sports'),
        ('Office','Office'),
        ('Food','Food'),
        ('Weekend Plan', 'Weekend Plan'),
        ('Other','Other'),
    ]
    category = models.CharField(max_length=100, choices=CAT_LIST, default="Other")

    def __str__(self):
        return f"{self.title} - {self.category}"

    def get_absolute_url(self):
        return reverse('notes:notes-detail', kwargs={'pk' : self.pk})
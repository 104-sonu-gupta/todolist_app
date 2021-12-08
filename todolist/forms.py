from django import forms
from django.forms import fields, models
from .models import TaskList

class Taskform(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']

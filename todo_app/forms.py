from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter task...'}),
        }
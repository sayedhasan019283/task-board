from django import forms
from . import models

class TodoWorkForm(forms.ModelForm):

    
    class Meta:
        model = models.TodoWorkModel
        fields = ['title', 'description', 'priority', 'task_complete_date']

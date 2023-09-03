from django import forms
from . import models

class ProjectForm(forms.ModelForm):

    
    class Meta:
        model = models.ProjectModel
        fields = ['project_title', 'Category']

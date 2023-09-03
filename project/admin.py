from django.contrib import admin
from django import forms
from . import models
# from . import forms
# Register your models here.

class ProjectModelAdminForm(forms.ModelForm):
    class Meta:
        model = models.ProjectModel
        fields = '__all__'  

admin.site.register(models.ProjectModel )
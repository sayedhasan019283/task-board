from django.contrib import admin
from django import forms
from . import models
# from . import forms
# Register your models here.

class TodoWorkModelAdminForm(forms.ModelForm):
    class Meta:
        model = models.TodoWorkModel
        fields = '__all__' 





admin.site.register(models.TodoWorkModel )
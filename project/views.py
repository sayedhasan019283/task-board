from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def create_project(request):
    if request.method == 'POST':
        # Create a form instance with the POST data
        project = forms.ProjectForm(request.POST)
        if project.is_valid():
            # due_date = work.cleaned_data['due_date']
            # Associate the authenticated user with the work item
            project_instance = project.save(commit=False)
            project_instance.user = request.user  # Assign the current user to the 'user' field
            project_instance.save()
            return redirect('profile')
    else:
        project = forms.ProjectForm()
    return render(request, 'project/create_project.html', {'form' : project})



        
    

from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoWorkModel
from project.models import ProjectModel
from . import forms
from django.shortcuts import render, get_object_or_404
from .models import TodoWorkModel
from project.models import ProjectModel
from task_management.models import TodoWorkModel
from django.db.models import Q
from django.utils import timezone 
# Other imports ...

def store_work(request, project_id):
    if request.method == 'POST':
        work = forms.TodoWorkForm(request.POST)
        if work.is_valid():
            project = get_object_or_404(ProjectModel, id=project_id)
            work_instance = work.save(commit=False)
            work_instance.project = project
            work_instance.save()
            return redirect('show_works', project_id)
    else:
        work = forms.TodoWorkForm()
    return render(request, 'work_entre.html', {'form': work})



def show_works(request, project_id):
    if request.user.is_authenticated:
        current_user = request.user
        project = get_object_or_404(ProjectModel, pk=project_id)
        
        # Retrieve tasks associated with the project and order them by priority
        tasks = project.project_task.all().order_by('task_complete_date')
        current_datetime = timezone.now()

        return render(request, 'show_work.html', {'tasks': tasks, 'project': project, 'current_datetime' : current_datetime})
    else:
        return render(request, 'work_entre.html')

def search(request):
    context = {}  # Define context with a default empty dictionary

    if 'keyword' in request.GET:
        keyword = request.GET('keyword')
        if keyword:
            data = TodoWorkModel.objects.order_by('-title').filter(Q(title__icontains=keyword) | Q(task_complete_date_name__icontains=keyword))
            context['tasks'] = data  # Assign the 'data' queryset to the 'tasks' key in the context
            print( 'print hear', data)

    return render(request, 'search.html', context)

def edit_work(request, id, project_id):
    work = get_object_or_404(TodoWorkModel, pk=id)
    
    form = forms.TodoWorkForm(instance=work)
    if request.method == 'POST':
        info = forms.TodoWorkForm(request.POST, instance=work)
        if info.is_valid():
            info.save()
            return redirect('show_works', project_id)
    return render(request, 'work_entre.html', {'form': form})

def delete_work(request, id, project_id):
    work = get_object_or_404(TodoWorkModel, pk=id)
    work.delete()
    return redirect('show_works', project_id)

def complete_task(request, id, project_id):

    return redirect('completed_work', project_id)

def completed_tasks(request,id, project_id):
    task = get_object_or_404(TodoWorkModel, pk=id)
    task.status = True
    task.save()
    tasks = TodoWorkModel.objects.filter(status=True, project__project_task=project_id)
    return redirect('show_works', project_id)

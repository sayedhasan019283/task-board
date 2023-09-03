from django.db import models
from django.contrib.auth.models import User
from project.models import ProjectModel

class TodoWorkModel(models.Model):

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, default=None, related_name='project_task')
    user_control = models.TextField(max_length=100, default="Default Value")
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(blank=True, auto_now_add=True)
    task_complete_date = models.DateTimeField()
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=MEDIUM 
    )
    
    def __str__(self):
        return self.title

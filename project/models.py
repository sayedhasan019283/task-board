from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProjectModel(models.Model):
    
    Software = 'Software'
    Website = 'Website'
    Application = 'Application'

    CATEGORY_CHOICES = [
        (Software, 'Software'),
        (Website, 'Website'),
        (Application, 'Application'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    id = models.IntegerField(primary_key=True)
    project_title = models.CharField(max_length=30)
    Category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default=Software 
    )
    
from django.urls import path
from . import views
urlpatterns = [
    # path('',  views.home),
    path('search/', views.search, name='search'),
    path('new_work/<int:project_id>/', views.store_work, name='storeWork'),
    path('show_work/<int:project_id>/', views.show_works, name='show_works'),
    path('edit_work/<int:id>/<int:project_id>/', views.edit_work, name='edit_work'),
    path('delete_work/<int:id>/<int:project_id>/', views.delete_work, name='delete_work'),
    path('complete_work/<int:id>/<int:project_id>/', views.completed_tasks, name='complete_work'),

    path('completed_work/', views.completed_tasks, name='completed_work'),
] 
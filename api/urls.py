from django.urls import path
from .views import get_tasks, completed_tasks, in_completed_tasks, create_task, update

urlpatterns = [
    path('tasks/', get_tasks),
    path('create/', create_task),
    path('completed/', completed_tasks),
    path('incompleted/', in_completed_tasks),
    path('update/<int:pk>/', update)
]

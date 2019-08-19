from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList),
    path('task/<int:id>', views.taskView),
    path('newTask/', views.newTask),
    path('edit/<int:id>', views.editTask),
    path('delete/<int:id>', views.deleteTask),
]

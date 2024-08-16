from django.urls import path

from . import views

urlpatterns = [
    # path('helloworld/', views.helloworld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"), # create
    path('edit/<int:id>', views.editTask, name="edit-task"), # update
    path('changestatus/<int:id>', views.changeStatus, name="change-status"), # editar o status
    path('delete/<int:id>', views.deleteTask, name="delete-task"), # delete
    # path('about', views.)
    # path('yourname/<str:name>', views.yourName, name="your-name")
]

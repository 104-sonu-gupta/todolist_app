from todolist import views
from django.urls import path

urlpatterns = [

    path('', views.todolist , name = 'todolist'),               # url will remember the name not path
    path('delete/<id>', views.delete , name = 'delete-task'),    # <variable> to map id from url
    path('edit/<id>', views.edit_task , name = 'edit-task'),   
    path('completed/<id>', views.completed , name = 'completed-task')   
]

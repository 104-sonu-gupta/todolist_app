from django.contrib import admin
from .models import TaskList

# Register your models here.

class TaskListAdmin(admin.ModelAdmin):
    list_display = ['id','user','task', 'done']
    # list_editable = ['done']

admin.site.register(TaskList, TaskListAdmin)
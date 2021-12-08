from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TaskList(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.task
 
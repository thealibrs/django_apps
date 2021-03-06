from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank = True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    ordering = ["complete"]
    
    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=200)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.work
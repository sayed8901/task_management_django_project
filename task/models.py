from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20)
    task_id = models.AutoField(primary_key=True)
    task_description = models.TextField()
    task_assign_date = models.DateField()

    def __str__(self):
        return self.task_name



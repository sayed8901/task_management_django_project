from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_id = models.AutoField(primary_key=True)
    task_description = models.TextField()
    task_assign_date = models.DateField()

    # many to many relationships with Category models
    category = models.ManyToManyField(Category)

    # 'is-completed' status initially set to 'False'
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.task_title

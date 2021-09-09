from django.db import models


# Create your models here.
class Task(models.Model):
    label = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    relates_to = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.label

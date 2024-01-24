from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.CharField(unique=True, max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"

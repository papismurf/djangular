from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    img = models.FileField(blank=False, null=False)
    uploaded_by = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.file.name
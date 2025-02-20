from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Text= models.TextField(max_length=100)
    Image= models.ImageField(upload_to='images/', blank=True, null=True)
    Created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.User.username}-{self.Text[:7]}'
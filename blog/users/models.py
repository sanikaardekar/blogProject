from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # cascade -  if user is deleted then delete the profile, but if we delete profile, user isnt deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} profile' 

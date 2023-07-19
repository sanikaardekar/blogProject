from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#sqlite db for dev and postgres for prod
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now) #actual function as default value so no ()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted then posts are also deleted not viceversa

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


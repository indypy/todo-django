from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=500)
    tags = TaggableManager()
    due_date = models.DateField()
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

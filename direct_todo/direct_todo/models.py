from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

class Task(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=500)
    tags = TaggableManager()
    due_date = models.DateField()

    def __unicode__(self):
        return self.title

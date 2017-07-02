from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

# Model for a meetup group that am following and for which
# want to load events. Stores the URL name of the meetup group.
class MeetupGroup(models.Model):
  url_name = models.TextField(unique=True)
  meetup_group_id = models.AutoField(primary_key = True)



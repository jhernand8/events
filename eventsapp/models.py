from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

# Model for a meetup group that am following and for which
# want to load events. Stores the URL name of the meetup group.
class MeetupGroup(models.Model):
  url_name = models.TextField(unique=True)
  meetup_group_id = models.AutoField(primary_key = True)

# Model for representing an event for a meetup group.
class MeetupEvent(models.Model):
  meetup_group_id = models.IntegerField()
  name = models.TextField()
  num_attendees = models.IntegerField()
  event_time_ms = models.IntegerField(blank=True, null=True)
  event_id = models.TextField()
  city = models.TextField(blank=True, null=True)
  event_url = models.TextField()
  meetup_event_id = models.AutoField(primary_key = True)


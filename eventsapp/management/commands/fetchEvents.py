from django.core.management.base import BaseCommand, CommandError
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from datetime import date
import json
import time
from urllib.request import urlopen
from eventsapp.models import MeetupGroup
from eventsapp.models import MeetupEvent

# Cron job that runs that fetches events for each group in MeetupGroups
# and saves upcoming meetups to the database. Also deletes meetups that
# have already passed.
class Command(BaseCommand):
  
  def handle(self, *args, **options):
    allGroups = MeetupGroup.objects.all()
    # remove events for groups that have been removed
    self.deleteOrphanedEvents(allGroups);
    for currGroup in allGroups:
      self.handleEventsForGroup(currGroup)
      time.sleep(0.4); # sleep so we don't get 429 error from Meetup
  
  def deleteOrphanedEvents(self, groups):

    allEvents = MeetupEvent.objects.all();
    for ev in allEvents:
      foundGroup = False;
      for gr in groups:
        if gr.meetup_group_id == ev.meetup_group_id:
          foundGroup = True;
          break;
      if not foundGroup:
        ev.delete();


  def handleEventsForGroup(self, group):
    # delete existing events for this group as we will refetch everything
    allEvents = MeetupEvent.objects.all()
    for event in allEvents:
      if event.meetup_group_id == group.meetup_group_id:
        event.delete();

    # now fetch and create events
    url = 'https://api.meetup.com/' + group.url_name + '/events?sign=true&page=10&key=573c6b134536b73f3234426519206e&&sign=true';
    print(url + "\n");
    jsonResp = "";
    try:
      resp = urlopen(url)
      jsonResp = json.load(resp)
    except:
      print("Failed loading/parsing: " + url);
      return;

    for ev in jsonResp:
      city = None
      if "location" in ev and "city" in ev["location"]:
        city = ev["location"]["city"]
      if "venue" in ev and "city" in ev["venue"]:
        city = ev["venue"]["city"]
      meetupEv = MeetupEvent(meetup_group_id = group.meetup_group_id,
                             name = ev["name"],
                             num_attendees = int(ev["yes_rsvp_count"]),
                             event_id = ev["id"],
                             event_url = ev["link"],
                             event_time_ms = int(ev["time"]),
                             city = city);
      meetupEv.save()





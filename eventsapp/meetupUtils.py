from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from datetime import date
import json
import time
from urllib.request import urlopen
from eventsapp.models import MeetupGroup
from eventsapp.models import MeetupEvent

# Helper to get the name of the group from the group url - makes request to meetup.
def fetchNameForGroup(groupUrl):
  url = 'https://api.meetup.com/' + groupUrl + '?sign=true&page=10&key=' + getApiKey() + '&sign=true&only=name';
  resp = urlopen(url)
  jsonResp = json.load(resp)
  if "name" in jsonResp:
    return jsonResp["name"]
  print("url" + url + ": " + jsonResp + "\n\n");
  return "";

# Helper to get the topics as a comma separated string.
def fetchTopicsForGroup(groupUrl):
  url = 'https://api.meetup.com/' + groupUrl + '?sign=true&page=10&key=' + getApiKey() + '&sign=true&only=topics&field=topics';
  resp = urlopen(url)
  jsonResp = json.load(resp)
  topicListStr = "";
  if "topics" in jsonResp:
    for currTopic in jsonResp["topics"]:
      if "name" in currTopic:
        topicListStr = currTopic["name"] + "," + topicListStr;
  return topicListStr; 


def getApiKey():
  return '573c6b134536b73f3234426519206e';

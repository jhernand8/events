from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
import json

from .models import Greeting
from .models import MeetupGroup

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    groups = MeetupGroup.objects.all();
    groupList = [];
    for group in groups:
      gr = {}
      gr["url"] = group.url_name
      gr["id"] = group.meetup_group_id
      groupList.append(gr)
    context = RequestContext(request, {
        'groups': mark_safe(json.dumps(groupList, cls=DjangoJSONEncoder))});
    return render(request, 'index.html', context)

def follow(request):
  meetupNames = request.POST.getlist('meetupgroup')
  allGroups = MeetupGroup.objects.all()
  for name in meetupNames:
    if name is None or name == "":
      continue
    
    # make sure there is not already an entry in groups
    exists = False
    for existGroup in allGroups:
      if existGroup.url_name == name:
        exists = True
        break
    if exists:
      continue

    # currently does not check the form itself for duplicates

    meetupGroup = MeetupGroup(name)
    meetupGroup.save()

  return HttpResponse('Success!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


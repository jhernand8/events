from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import MeetupGroup

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

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


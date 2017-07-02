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
  for name in meetupNames:
    meetupGroup = MeetupGroup(name)
    meetupGroup.save()
  return HttpResponse('Success!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


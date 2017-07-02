# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('eventsapp', '0001_initial'),
        ('eventsapp', '002')
    ]

    operations = [
        migrations.CreateModel(
            name='MeetupEvent',
            fields=[
                ('meetup_group_id', models.IntegerField(unique=False, verbose_name='Meetup Group ID foreign key')),
                ('name', models.TextField(unique=False, verbose_name='Meetup Event Name')),
                ('num_attendees', models.IntegerField(unique=False, verbose_name='Number of attendees')),
                ('event_date', models.DateTimeField(unique=False, verbose_name='Event date')),
                ('event_id', models.TextField(unique=False, verbose_name='Meetup event id in Meetup')),
                ('city', models.TextField(unique=False, verbose_name='Meetup  location city')),
                ('event_url', models.TextField(unique=True, verbose_name='Meetup url for event')),
                ('meetup_event_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Meetup event ID')),
            ],
        ),
    ]

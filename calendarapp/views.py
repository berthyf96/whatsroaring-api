#!/usr/bin/python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.urls import reverse
from django.core.serializers import serialize
from CASClient import CASClient
import json
import os
import CASTest
from .forms import AddEventForm, AddOrgForm
from .models import Event, Category, Organization

# Create your views here.
def home(request):

	if request.GET.get('login'):
		cas = CASClient(request)
		return cas.Authenticate()

	return render(request, 'calendarapp/home.html', {})

def getEvents(request):
	selected_events = Event.objects.all()
	location = None
	# decode AJAX request, which should contain location request
	if request.body.decode('utf-8'):
		location = json.loads(request.body.decode('utf-8')).get('location')
	if location:
		selected_events = Event.objects.filter(location=location)
	eventsJson = serialize('json', selected_events)
	data = {'Events_JSON': eventsJson}
	return JsonResponse(data)


def createEvent(org, cat, name, start_datetime, end_datetime, location, is_free, website, description):
	e = Event(org=org, category=cat, name=name, start_datetime=start_datetime, \
		end_datetime=end_datetime, location=location, is_free=is_free, website=website, \
		description=description)
	e.save()

def createOrganization(name):
	o = Organization(name=name)
	o.save()

class CalView(generic.ListView):
    template_name = 'calendarapp/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.all()

class DetailView(generic.DetailView):
    model = Event
    template_name = 'calendarapp/detail.html'

class AddEventView(generic.TemplateView):
	template_name = 'calendarapp/addevent.html'

	def get(self, request):
		form = AddEventForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):

		form = AddEventForm(request.POST)

		if form.is_valid():
			print('valid')
			form.save()
			form = AddEventForm()
			return redirect('calendarapp:addevent')
		else:
			print('errors')
			print(form.errors)


		args = {'form': form}
		return render(request, self.template_name, args)

class AddOrgView(generic.TemplateView):
	template_name = 'calendarapp/addorg.html'

	def get(self, request):
		form = AddOrgForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):

		form = AddOrgForm(request.POST)

		if form.is_valid():
			print('valid')
			form.save()
			form = AddOrgForm()
			return redirect('calendarapp:addorg')
		else:
			print('errors')
			print(form.errors)

		args = {'form': form}
		return render(request, self.template_name, args)

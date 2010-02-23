from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from Alter_Need.have.models import Item, Location
from geopy import geocoders
import string

def register(request):
	error = ""
	if (request.method == 'POST'):
		if User.objects.filter(username__exact=(request.POST['username'])):
			error = "Username %s already exists" % request.POST['username']
		elif not (request.POST['pass1'] == request.POST['pass2']):
			error = "Passwords dont match"
		elif (not request.POST['username'] or not request.POST['pass1'] or not request.POST['pass2'] or not request.POST['email']):
			error = "Some mandatory fields left blank"
		else:
			user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['pass1'])
			user.is_staff = False
			user.save()
			user = auth.authenticate(username=request.POST['username'], password=request.POST['pass1'])
			auth.login(request, user)
			return HttpResponseRedirect("/have/")

	return render_to_response("registration/register.html", {'error': error})

@login_required
def profile(request): 
	list = Item.objects.filter(user__exact=request.user.id)
	locs = Location.objects.filter(user__exact=request.user.id)
	return render_to_response("have/profile.html", {'list': list, 'locs': locs})

@login_required
def addLoc(request):
	place = string.lower(request.POST['location'])
	locn = Location(loc=place, user_id=request.user.id)
	locn.save()
	return HttpResponseRedirect("/have/")

@login_required
def addItem(request):
	item = Item(description=string.lower(request.POST["description"]), user_id=request.user.id)
	item.save()
	return HttpResponseRedirect("/have/")


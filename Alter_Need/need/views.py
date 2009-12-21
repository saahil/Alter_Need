from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from Alter_Need.have.models import Item, Location
from googlemaps import GoogleMaps
import string

def weight_of(text, key):
	doc_list = string.split(text)
	key_list = string.split(key)

	tot_weight = 0

	for cur in key_list:
		if cur in doc_list:
			tot_weight = tot_weight + len(cur)

	return tot_weight

def search_sort(doc_list, key):
	found = []
	for cur in doc_list:
		if weight_of(cur.description, key) is not 0:
			if not found:
				found.append(cur)
			else:
				i = len(found) - 1
				found.append("")
				while (weight_of(found[i], key) < weight_of(cur, key)) and (i>=0):
					found[i+1] = found[i]
					i = i-1
				found[i+1] = cur
	return found

def in_vic(lat1, lng1, lat2, lng2):
	if (abs(lat1-lat2)<=5.0) and (abs(lng1-lng2)<=5.0):
		return True
	else:
	 	return False

def lookup(request):
	if (request.method == 'POST'):
		gmaps = GoogleMaps()
		locs = Location.objects.all()
		close_by = []
		for cur in locs:
			cur_lat = cur.lat
			cur_lng = cur.lng
			if (cur == string.lower(request.POST['where'])):
				close_by.append(cur.user)
			else:
				latitude, longitude = gmaps.address_to_latlng(request.POST['where'])
				if in_vic(float(cur_lat), float(cur_lng), latitude, longitude):
					close_by.append(cur.user)

		items = Item.objects.filter(user__in=close_by)
		list = search_sort(items, string.lower(request.POST['what']))
		return render_to_response("need/lookup.html", {"list": list})

	return render_to_response("need/lookup.html")

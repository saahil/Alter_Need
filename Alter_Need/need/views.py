from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from Alter_Need.have.models import Item, Location
from geopy import geocoders, distance
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

#def in_vic(lat1, lng1, lat2, lng2):
#	lat2 = float(lat2)
#	lng2 = float(lng2)
#	if (abs(lat1-lat2)<=5.0) and (abs(lng1-lng2)<=5.0):
#		return True
#	else:
#	 	return False

def lookup(request):
	if (request.method == 'POST'):
		gmaps = geocoders.Google()
		locs = Location.objects.all()
		close_by = []
		markers = gmaps.geocode(request.POST['where'], exactly_one=False)
		for cur in locs:
			if (cur == string.lower(request.POST['where'])):
				close_by.append(cur.user)
			else:
				for _, cur_loc in gmaps.geocode(cur, exactly_one=False):
					for _, marker in markers:
						mile = distance.distance(marker, cur_loc).miles
						if(mile <= 80):
							close_by.append(cur.user)

		items = Item.objects.filter(user__in=close_by)
		list = search_sort(items, string.lower(request.POST['what']))
		return render_to_response("need/lookup.html", {"list": list})

	return render_to_response("need/lookup.html")

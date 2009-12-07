from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	description = models.TextField()
	user = models.ForeignKey(User)

	def __str__(self):
		return self.description

class Location(models.Model):
	loc = models.CharField(max_length=50)
	lat = models.DecimalField(max_digits=20, decimal_places=15)
	lng = models.DecimalField(max_digits=20, decimal_places=15)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.loc


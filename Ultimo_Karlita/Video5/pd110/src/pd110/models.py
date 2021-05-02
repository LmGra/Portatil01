from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrado(models.Model):
	nombre = models.CharField(max_Length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self): #Python3
		return self.email
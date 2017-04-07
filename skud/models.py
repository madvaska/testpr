from django.db import models
from django.utils import timezone

# Create your models here.

class Emp(models.Model):
	fname = models.CharField(max_length=100)
	sname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	publish_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.lname


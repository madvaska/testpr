from django.db import models
from django.utils import timezone

# Create your models here.

class Dep(models.Model):
	short_name = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100) 
	parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Emp(models.Model):
	fname = models.CharField(max_length=100)
	sname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	dep = models.ForeignKey(Dep,blank=True, null=True, on_delete=models.SET_NULL)
	publish_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.lname


from django.db import models
from users.models import OjUser

class Detail(models.Model):
	def __unicode__(self):
		return self.pid
	pid = models.CharField(max_length=10)
	total = models.IntegerField(default=0)
        tle = models.IntegerField(default=0)
	acc = models.IntegerField(default=0)
	wa = models.IntegerField(default=0)
	ce = models.IntegerField(default=0)
	rte = models.IntegerField(default=0)
	accuracy = models.FloatField(default=0.0)
	

class Problem(models.Model):
	def __unicode__(self):
		return self.pid
	pid = models.CharField(primary_key=True,max_length=10)
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=10000)
	sample_input = models.TextField(max_length=10000)
	sample_output = models.TextField(max_length=10000)
	explanation = models.TextField(max_length=10000)
	is_active = models.BooleanField(default=False)
	details = models.ForeignKey(Detail)
	testfiles = models.IntegerField(default=0)
	time_limit = models.FloatField(default=0)
        created_by = models.ForeignKey(OjUser,blank=True,null=True)
	

class Submission(models.Model):
	def __unicode__(self):
		return str(self.sid)
	sid= models.AutoField(primary_key=True)
	prob = models.ForeignKey(Problem)
	code = models.FileField(upload_to='submissions',blank=True,null=True)
	language = models.CharField(max_length=10)
	subtime = models.DateTimeField()
	status = models.CharField(max_length=20,default="waiting")
	extime = models.FloatField(default=0)
	user = models.ForeignKey(OjUser)
        errorcode = models.TextField(max_length=1000)
	
	




# Create your models here.

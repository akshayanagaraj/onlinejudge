from django.db import models
from django.contrib.auth.models import User

class OjUser(User):
	gender = models.CharField(max_length=3,blank=True,null=True)
	reg_no = models.CharField(max_length=23,blank=True,null=True)
	tot_sub = models.IntegerField(default=0)
	succ_sub = models.IntegerField(default=0)
	points = models.FloatField(default=0)
        rank = models.IntegerField(default=1)
        is_loggedin = models.BooleanField(default=False)
        ex_time = models.FloatField(default=0.0)
        is_creator = models.BooleanField(default=False)
	


# Create your models here.

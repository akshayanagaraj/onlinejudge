from django.db import models
from django.contrib.auth.models import User

class OjUser(User):
	gender = models.CharField(max_length=3,blank=True,null=True)
	reg_no = models.CharField(max_length=23,blank=True,null=True)


# Create your models here.

from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.user.username

class Request(models.Model):
	poster = models.ForeignKey(UserProfile)
	request = models.TextField()
	posted_on = models.DateTimeField(auto_now_add=True)
	

	def __unicode__(self):
		return self.
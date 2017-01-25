from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
	is_donor = models.BooleanField(default=False, verbose_name='Donor')
	is_recipient = models.BooleanField(default=False, verbose_name='Recipient')
	bio = models.TextField(blank=True)
	services = models.TextField(blank=True)
	image = models.ImageField(upload_to='profile_images', blank=True)
	shop = models.CharField(max_length=25, blank=True)
	#location = models


# class Request(models.Model):
# 	poster = models.ForeignKey(User)
# 	title = models.CharField(max_length=128)
# 	request = models.TextField()
# 	posted_on = models.DateTimeField(auto_now_add=True)
	

# 	def __unicode__(self):
# 		return self.title
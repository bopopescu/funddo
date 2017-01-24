from django import forms
from models import Request, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture', 'bio')

class RequestForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter a title")
	request = forms.CharField(widget=forms.Textarea(), required=True)


	class Meta:
		model = Request
		fields = ('title', 'request')
		exclude = ('poster',)
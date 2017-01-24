from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import UserProfile, Request
from django.contrib.auth.models import User
from forms import RequestForm, UserForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def index(request):
	context_dict = {}
	return render(request, 'index.html', context_dict)


def about(request):
	context_dict = {}
	return render(request, 'about.html', context_dict)

def make_request(request):
	if request.method == "POST":
		form = RequestForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.poster = request.user
			post.posted_on = datetime.now()
			post.save()
			return HttpResponseRedirect('/')
	else:
		form = RequestForm()
	return render(request, 'make_request.html', {'form': form})
def requests(request):
	context_dict = {}
	content = Request.objects.get(request=request)

	return render(request, 'requests.html', context_dict)


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save() 

			profile = profile_form.save(commit=False)

			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'register.html', {'user_form' : user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Your account is inactive')
		else:
			print "Invalid login details : {0},{1}".format(username, password)
			return HttpResponse('Your login credentials were wrong')

	else:
		return render(request, 'login.html', {})
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, user_passes_test

# def home(request):
# 	return render_to_response('home.html')

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/awarie/')
	else:
		return HttpResponseRedirect('/invalid/')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Admin').count() == 0, login_url='/panel')
@user_passes_test(lambda u: u.groups.filter(name='Zgłaszający').count() == 0, login_url='/dashboard')
def loggedin(request):
	return render_to_response('loggedin.html',{'user_name' : request.user.username})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='SUR').count() == 0, login_url='/loggedin')
@user_passes_test(lambda u: u.groups.filter(name='Zgłaszający').count() == 0, login_url='/dashboard')
def panel(request):
	return render_to_response('panel.html',{'user_name' : request.user.username})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='SUR').count() == 0, login_url='/loggedin')
@user_passes_test(lambda u: u.groups.filter(name='Admin').count() == 0, login_url='/panel')
def dashboard(request):
	return render_to_response('dashboard.html',{'user_name' : request.user.username})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login/')

def invalid_login(request):
	return render_to_response('invalid_login.html')
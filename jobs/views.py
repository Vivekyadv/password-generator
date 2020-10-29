from django.shortcuts import render
from .models import Job
import random

def home(request, *args, **kwargs):
	jobs = Job.objects
	return render(request,'jobs/home.html', {'jobs':jobs})

def gen_pswrd(request, *args, **kwargs):
	return render (request, 'jobs/gen_pswrd.html')

def password(request, *args, **kwargs):

	characters = list('abcdefghijklmnopqrstuvwxyz')
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()_+|-='))

	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))


	length = int(request.GET.get('length', 12))
	thepassword = ''

	for x in range(length):
		thepassword += random.choice(characters)

	return render (request, 'jobs/password.html', {'password': thepassword})

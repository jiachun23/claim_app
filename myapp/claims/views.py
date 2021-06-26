from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login

def login(request):

	return render(request, 'views/login.html')


def index(request):

	form = ClaimForm()

	if request.method == 'POST':
		form = ClaimForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'views/index.html', context)





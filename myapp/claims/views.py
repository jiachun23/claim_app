from django.shortcuts import render
from .forms import *
from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *


def viewlist(request):
	
	if not request.user.is_authenticated:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

	entry = User.objects.get(pk=request.user.id)

	claim_obj = Claim.objects.filter(fk_user=entry)

	context = {'claim': claim_obj}
	
	return render(request, 'views/viewlist.html', context)


def index(request):

	entry = User.objects.get(pk=request.user.id)

	thisdict = {
		'fk_user': entry
	}

	if request.method=="GET" and request.GET['pk'] is not None:
		pk = request.GET['pk']
		claim_obj = Claim.objects.filter(id=pk)
		
		form = ClaimForm(instance=claim_obj[0])
		
		context = {'form':form,
				   'pk':pk}
		return render(request, 'views/index.html', context)

	form = ClaimForm(thisdict)

	if request.method=="POST" and request.GET['pk'] is not None:
		pk = request.GET['pk']
		claim_obj = Claim.objects.get(id=pk)

		for attr, value in request.POST.items(): 
			if attr == 'fk_user':
				continue
		
			setattr(claim_obj, attr, value)

		claim_obj.save()

		return HttpResponseRedirect('/claims/view')

	if request.method == 'POST':
		print(request.GET)

		form = ClaimForm(request.POST, request.FILES)
		
		print(request.POST)
	
		
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/claims/view')

	context = {'form':form}
	return render(request, 'views/index.html', context)








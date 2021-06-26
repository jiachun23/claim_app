from django.forms import ModelForm
from .models import *
from django import forms
from django.forms.fields import DateField

class ClaimForm(forms.ModelForm):
	class Meta:
		model = Claim
		fields = '__all__'
		exclude = ('Claim_Status',)
		widgets = {
						'Date_of_accident': forms.DateInput(
							format=('%m-%d-%Y'),
							attrs={'class': 'form-control', 
								'placeholder': 'Select a date',
								'type': 'date'
								}),
					}
		
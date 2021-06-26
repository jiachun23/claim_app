from django.forms import ModelForm
from .models import *

class ClaimForm(ModelForm):
	class Meta:
		model = Claim
		fields = '__all__'


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'


# class Admin_ClaimForm(ModelForm):
# 	class Meta:
# 		model = Admin_Claim
# 		fields = '__all__'
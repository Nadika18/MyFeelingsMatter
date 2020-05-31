from .models import Patient

from django import forms

class CreatePatient(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['name','email','symptoms','gender']

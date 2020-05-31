from django.shortcuts import render,redirect
from . import forms

def home(request):
	return render(request,'mentor/home.html')

def patient_create(request):
	form = forms.CreatePatient()
	if request.method == 'POST':
		form = forms.CreatePatient(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mentor-home')
	else:
		form = forms.CreatePatient()
	
	return render(request, 'mentor/form.html',{'form':form})

def dep(request):
	return render(request,'mentor/depression.html')
def s(request):
	return render(request,'mentor/symp.html')
def v(request):
	return render(request,'mentor/motivate.html')

# Create your views here.

from django.shortcuts import render,redirect
from . import forms

def home(request):
	return render(request,'mentor/home.html')
<<<<<<< HEAD
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
=======
def form(request):
	return render(request,'mentor/form.html')
def dep(request):
	return render(request,'mentor/depression.html')

>>>>>>> 22f1f180c2f26b59ac5008d5a948eb268b8d0efb
# Create your views here.

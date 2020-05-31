from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'mentor/home.html')
def form(request):
	return render(request,'mentor/form.html')

# Create your views here.

from django.urls import path
from . import views
urlpatterns=[
	path('',views.home,name='mentor-home'),
	path('create',views.patient_create, name="mentor-form"),
	path('depression.html',views.dep, name="mentor-dep")

]
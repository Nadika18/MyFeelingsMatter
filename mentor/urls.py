from django.urls import path
from . import views
urlpatterns=[
	path('',views.home,name='mentor-home'),
	path('form.html',views.form, name="mentor-form"),
	path('depression.html',views.dep, name="mentor-dep")
]
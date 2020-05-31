from django.urls import path
from . import views
urlpatterns=[
	path('',views.home,name='mentor-home'),
<<<<<<< HEAD
	path('create',views.patient_create, name="mentor-form"),
=======
	path('form.html',views.form, name="mentor-form"),
	path('depression.html',views.dep, name="mentor-dep")
>>>>>>> 22f1f180c2f26b59ac5008d5a948eb268b8d0efb
]
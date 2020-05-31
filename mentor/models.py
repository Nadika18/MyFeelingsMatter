from django.db import models

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	symptoms = models.TextField()
	gender = models.CharField(max_length=10)

	def __str__(self):
		return self.email
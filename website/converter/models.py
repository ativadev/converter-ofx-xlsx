from django.db import models
from os import path

# Create your models here.
class Upload(models.Model):
	document = models.FileField(upload_to='uploads')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	file_name = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.file_name


class Output(models.Model):
	document = models.FileField(upload_to='output')
	created_at = models.DateTimeField(auto_now_add=True)
	original_file = models.ForeignKey(Upload, on_delete=models.CASCADE)
	file_name = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.file_name

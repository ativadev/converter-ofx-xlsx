from django.db import models
from os import path

import uuid

# Create your models here.
class Upload(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	document = models.FileField(upload_to='uploads')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	file_name = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return f'{self.id} - {self.file_name}'

class Output(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	document = models.FileField(upload_to='output')
	created_at = models.DateTimeField(auto_now_add=True)
	original_file = models.ForeignKey(Upload, on_delete=models.CASCADE)
	file_name = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return f'{self.id} - {self.file_name}'

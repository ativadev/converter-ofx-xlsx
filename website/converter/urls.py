from django.urls import path
from . import views

app_name = 'converter'
urlpatterns = [
	path('', views.index, name='index'),
	path('resultado/<int:file_id>/', views.result, name='resultado'),
	path('download/<int:file_id>', views.download, name='download'),
	path('upload', views.upload, name='upload')
]

from django.urls import path
from . import views

app_name = 'converter'
urlpatterns = [
	path('', views.index, name='index'),
	path('download/<str:file_id>', views.download, name='download')
]

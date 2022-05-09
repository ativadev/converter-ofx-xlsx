from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Upload, Output
from .forms import DocumentForm, handle_uploaded_file

# Create your views here.
def index(request):
	if request.method == 'POST' and request.FILES:
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				uploaded_file = request.FILES['file']
				print(type(uploaded_file))
				file = Upload(document=uploaded_file, file_name=uploaded_file.name)
				file.save()
				new_doc = handle_uploaded_file(uploaded_file)
				print(type(new_doc))
				print('SAIU DA FUNÇÃO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
				output_file = Output(document=new_doc, file_name=new_doc.name, original_file=file)
				print(type(output_file))
				output_file.save()
				# uploaded_file = request.FILES['file']
				# fs = FileSystemStorage()
				# filename = fs.save(uploaded_file.name, uploaded_file)
				# uploaded_file_url = fs.url(filename)
				# print(uploaded_file_url)
				"""FAZ A CONVERSÃO DO ARQUIVO"""
				return HttpResponseRedirect('resultado/1')
			except:
				return a

	else:
		form = DocumentForm()
	latest_uploads = Upload.objects.order_by('-uploaded_at')[:5]
	context = {
		'latest_uploads': latest_uploads,
		'form': form
	}
	return render(request, 'converter/index.html', context)

def result(request, file_id):
	file = get_object_or_404(Upload, pk=file_id)
	return render(request, 'converter/result.html', { 'file': file })


def download(request, file_id):
	return HttpResponse(f'Baixando arquivo {file_id}')

def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			print(request.FILES)
			return HttpResponseRedirect('/resultado/1')
	else:
		form = UploadFileForm()
	return HttpResponse('Foi!')

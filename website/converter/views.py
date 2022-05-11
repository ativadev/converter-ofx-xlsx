from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from os import path

import website.settings as settings
from .models import Upload, Output
from .forms import DocumentForm, handle_uploaded_file

# Create your views here.
def index(request):
	if request.method == 'POST' and request.FILES:
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				uploaded_file = request.FILES['file']
				file = Upload(document=uploaded_file, file_name=uploaded_file.name)
				file.save()
				new_doc = handle_uploaded_file(uploaded_file)
				output_file = Output(document=new_doc, file_name=new_doc.name, original_file=file)
				output_file.save()
				return HttpResponseRedirect(f'download/{output_file.id}')
			except:
				return a

	else:
		form = DocumentForm()
	latest_uploads = Upload.objects.order_by('-uploaded_at')[:10]
	context = {
		'latest_uploads': latest_uploads,
		'form': form
	}
	return render(request, 'converter/index.html', context)

def download(request, file_id):
	file = get_object_or_404(Output, pk=file_id)
	relative_path = f'{file.document}'
	file_path = path.join(settings.MEDIA_ROOT, relative_path)
	if path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type='application/vnd.ms-excel')
			response['Content-Disposition'] = 'inline; filename=' + path.basename(file_path)
			return response
	return render(request, 'converter/result.html', { 'file': file })

from crispy_forms.helper import FormHelper
from ofxparse import OfxParser
from django import forms
from os import path
import xlsxwriter
import codecs
import sys
import io

from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Upload

class DocumentForm(forms.Form):
	helper = FormHelper()
	file = forms.FileField(label=False, required=True, allow_empty_file=False, widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.txt, .ofx'}))

	class Meta:
		model = Upload
		fields = ('document',)

def handle_uploaded_file(f):
	total = bytes()
	for chunk in f.chunks():
		total += chunk

	file_io = io.BytesIO(total)
	data = get_data_from_ofx(file_io)
	new_io = create_sheet_from_data(data)
	output_name = f'{f.name.split(".")[0]}_OUTPUT.xls'
	new_doc = InMemoryUploadedFile(new_io, "FileField", output_name, "application/vnd.ms-excel", sys.getsizeof(new_io), None)
	return new_doc


def get_data_from_ofx(ofx_file):
	obj = OfxParser.parse(ofx_file)

	account = obj.account
	statement = account.statement
	transactions = statement.transactions
	resultado = [[['DATA'], ['DESCRIÇÃO'], ['DOC'], ['SAÍDA'], ['ENTRADA']]]

	for transaction in transactions:
		if transaction.amount < 0:
			resultado.append([[transaction.date], [''], [transaction.memo], [abs(transaction.amount)], ['']])
		else:
			resultado.append([[transaction.date], [''], [transaction.memo], [''], [transaction.amount]])



	return resultado

def create_sheet_from_data(data):
	output = io.BytesIO()
	planilha = xlsxwriter.Workbook(output)
	aba = planilha.add_worksheet()

	for linha in range(len(data)):
		for coluna in range(len(data[linha])):
			valor = data[linha][coluna][0]
			aba.write(linha, coluna, valor)

	planilha.close()
	output.seek(0)

	return output

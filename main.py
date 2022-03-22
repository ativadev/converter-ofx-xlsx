# Biblioteca pra processar os arquivos
from ofxparse import OfxParser
import xlsxwriter
import codecs
import os

def ler_arquivos(pasta):

	arquivos = []

	for filename in os.listdir(pasta):
		f = os.path.join(pasta, filename)
		if os.path.isfile(f):
			with codecs.open(f) as fileobj:
				ofx = OfxParser.parse(fileobj)
				arquivos.append({'nome': filename, 'dados': ofx})

	return arquivos


def gerar_planilha(obj):

	account = obj.account
	statement = account.statement
	transactions = statement.transactions
	resultado = [[['DATA'], ['TIPO'], ['VALOR'], ['MEMO'],['NOME']]]

	for transaction in transactions:
		resultado.append([[transaction.date],[transaction.type],[transaction.amount],[transaction.memo],[transaction.payee]])

	return resultado


def escrever_planilha(dados, pasta, nome):

	planilha = xlsxwriter.Workbook(f'{pasta}/{nome}_saida.xlsx')
	aba = planilha.add_worksheet()

	for linha in range(len(dados)):
		for coluna in range(len(dados[linha])):
			valor = dados[linha][coluna][0]
			aba.write(linha, coluna, valor)

	planilha.close()


def main():
	arquivos = ler_arquivos('entrada')
	for arquivo in arquivos:
		planilha = gerar_planilha(arquivo['dados'])
		escrever_planilha(planilha, 'saída',arquivo['nome'])

main()
#with open('saída.csv', 'a') as out:
    #out.write(resultado)

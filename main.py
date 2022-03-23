# Biblioteca pra processar os arquivos
from ofxparse import OfxParser
import xlsxwriter
import codecs
import os
import time

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
	resultado = [[['DATA'], ['MEMO'], ['TIPO'], ['SAÍDA'], ['ENTRADA']]]

	for transaction in transactions:
		if transaction.amount < 0:
			resultado.append([[transaction.date], [transaction.memo], [transaction.type], [abs(transaction.amount)], ['']])
		else:
			resultado.append([[transaction.date], [transaction.memo], [transaction.type], [''], [transaction.amount]])
	return resultado


def escrever_planilha(dados, pasta, nome):

	planilha = xlsxwriter.Workbook(f'{pasta}/{nome}_saida.xlsx')
	aba = planilha.add_worksheet()

	for linha in range(len(dados)):
		for coluna in range(len(dados[linha])):
			valor = dados[linha][coluna][0]
			aba.write(linha, coluna, valor)

	planilha.close()
	return True


def main():
	print('[CONVERSOR] Iniciando conversão...')
	arquivos = ler_arquivos('entrada')
	gerados = []
	for arquivo in arquivos:
		nome = arquivo['nome']
		print(f'[CONVERSOR] Convertendo arquivo {nome}...')
		planilha = gerar_planilha(arquivo['dados'])
		gerados.append({ nome: escrever_planilha(planilha, 'saída',arquivo['nome'])})

	print(f'[SUCESSO] Foram convertidos {len(gerados)} arquivos!')
	print('[SUCESSO] Verifique a pasta SAÍDA!')
	time.sleep(3)


def teste():
	arquivos = ler_arquivos('entrada')
	gerados = []
	for arquivo in arquivos:
		dados = arquivo['dados'].account.statement.transactions[0]
		print(dados.__dict__)


if __name__ == '__main__':
	main()

#with open('saída.csv', 'a') as out:
    #out.write(resultado)

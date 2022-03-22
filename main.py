# Biblioteca pra processar os arquivos
from ofxparse import OfxParser
import xlsxwriter
import codecs

with codecs.open('entrada.ofx') as fileobj:
	ofx = OfxParser.parse(fileobj)

account = ofx.account
statement = account.statement
transactions = statement.transactions
resultado = [[['DATA'], ['TIPO'], ['VALOR'], ['MEMO'],['NOME']]]

for transaction in transactions:
	resultado.append([[transaction.date],[transaction.type],[transaction.amount],[transaction.memo],[transaction.payee]])

planilha = xlsxwriter.Workbook('saida.xlsx')

aba = planilha.add_worksheet()

for linha in range(len(resultado)):
	for coluna in range(len(resultado[linha])):
		valor = resultado[linha][coluna][0]
		aba.write(linha, coluna, valor)

planilha.close()

#with open('saída.csv', 'a') as out:
    #out.write(resultado)

import mysql.connector
import funcs.checagensProdutos as armazem
from funcs.despesas import despesasMensais
from funcs.lucro import lucroBrutoMensal, calculaLucroLiquido
from funcs.funcsUtils import criarIntervaloDate

farmaciaDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='farmacia'
)
SQLCursor = farmaciaDB.cursor()

print('---Checagem de lucro & despesas por mês---')
ano = input('Insira o ano: ')
mes = input('Insira o mês: ')
dp = despesasMensais(f'{ano}-{mes}', SQLCursor)
lb = lucroBrutoMensal(f'{ano}-{mes}', SQLCursor)
print(dp)
print(lb)
print(calculaLucroLiquido(lb, dp))
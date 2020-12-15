from decimal import *
from funcs.funcsUtils import criarIntervaloDate

def lucroBrutoMensal(data, SQLCursor):
    lucroBrutoVendas = Decimal('0')
    lucroBrutoEntregas = Decimal('0')
    lucroBrutoTotal = Decimal('0')

    SQLAcharIdEntreDatas = ('SELECT id '
                            'FROM historico_vendas '
                            'WHERE dataVenda BETWEEN %s and %s')
    acharIdEntreDatasValues = criarIntervaloDate(data)
    SQLCursor.execute(SQLAcharIdEntreDatas, acharIdEntreDatasValues)
    resultado = SQLCursor.fetchall()

    try:
        idInicial = resultado[0][0]
        idFinal = resultado[-1][0]
    except:
        return({'lucro_bruto_total': 0, 'lucro_bruto_vendas': 0, 'lucro_bruto_entregas': 0})

    SQLLucroBrutoVendas = ('SELECT valor_desconto_aplicado, id_entrega '
                        'FROM historico_vendas '
                        'WHERE id BETWEEN %s AND %s')
    lucroBrutoVendasValues = idInicial, idFinal
    SQLCursor.execute(SQLLucroBrutoVendas, lucroBrutoVendasValues)
    lucroBrutoVendasResultado = SQLCursor.fetchall()
    for item in lucroBrutoVendasResultado:
        lucroBrutoVendas += item[0]

    #consertar between
    SQLLucroBrutoEntregas = ('SELECT valor_frete '
                            'FROM entrega '
                            'WHERE id_venda BETWEEN %s AND %s')
    lucroBrutoEntregasValues = (idInicial, idFinal)             
    SQLCursor.execute(SQLLucroBrutoEntregas, lucroBrutoEntregasValues)
    lucroBrutoEntregasResultado = SQLCursor.fetchall()
    for item in lucroBrutoEntregasResultado:
        lucroBrutoEntregas += item[0]

    lucroBrutoTotal = lucroBrutoEntregas + lucroBrutoVendas
    return({'lucro_bruto_total': lucroBrutoTotal, 'lucro_bruto_vendas': lucroBrutoVendas, 'lucro_bruto_entregas': lucroBrutoEntregas})

def calculaLucroLiquido(dictLucro, dictDespesa):
    lucroLiquido = dictLucro['lucro_bruto_total'] - dictDespesa['custo_total']
    return(lucroLiquido)
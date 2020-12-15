from decimal import *

def despesasMensais(data, SQLCursor):
    custoFuncionarios = Decimal('0')
    custoRemedios = Decimal('0')
    custoGasolina = Decimal('0')
    custoTotal = Decimal('0')

    SQLSalarios = 'SELECT salario, comissao FROM funcionario'
    SQLCursor.execute(SQLSalarios, )
    salarioFuncionariosResultado = SQLCursor.fetchall()
    for i,item in enumerate(salarioFuncionariosResultado):
        custoFuncionarios += item[0] + item[1]

    #consertar o between (salvar em uma variavel para usar no proximo SQL)
    SQLPrecoProdutoFornecedor = ('SELECT venda.qtd_produto_vendido, preco_produto_fornecedor.preco '
                                'FROM farmacia.venda '
                                'INNER JOIN preco_produto_fornecedor ON venda.id_produto_vendido = preco_produto_fornecedor.id_produto '
                                'WHERE venda.id_venda BETWEEN 1 AND 100')
    SQLCursor.execute(SQLPrecoProdutoFornecedor, )
    PrecoProdutoFornecedorResultado = SQLCursor.fetchall()
    for item in PrecoProdutoFornecedorResultado:
        custoRemedios += item[0] * item[1]

    #consertar o between
    SQLPrecoGasolina = ('SELECT custo_gasolina '
                        'FROM entrega '
                        'WHERE id_venda BETWEEN 1 AND 20')
    SQLCursor.execute(SQLPrecoGasolina, )
    PrecoGasolinaResultado = SQLCursor.fetchall()
    for item in PrecoGasolinaResultado:
        custoGasolina += item[0]

    custoTotal = custoFuncionarios + custoGasolina + custoRemedios

    return({'custo_total': custoTotal, 'custoFuncionarios': custoFuncionarios, 'custoGasolina': custoGasolina, 'custoRemedios': custoRemedios})
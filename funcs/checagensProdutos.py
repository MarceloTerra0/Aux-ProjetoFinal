def retornaEstoqueFarmacia(nomeFarmacia, SQLCursor):
    SQLArmazemProdutos = ('SELECT farmacias.nome_farmacia, produto.nome, armazem.qtd_produto '
            'FROM armazem '
            'INNER JOIN produto ON armazem.id_produto = produto.id '
            'INNER JOIN farmacias ON armazem.id_farmacia = farmacias.id_farmacia '
            'WHERE farmacias.nome_farmacia LIKE %s'
            'ORDER BY farmacias.nome_farmacia'
        )
    SQLValues = (nomeFarmacia, )
    SQLCursor.execute(SQLArmazemProdutos, SQLValues, )
    ArmazemProdutos = SQLCursor.fetchall()
    return([item for item in ArmazemProdutos])

def retornaPrecoFornecedor(idProduto, SQLCursor):
        SQLPrecoProdutoFornecedor = 'SELECT preco_produto_fornecedor.preco FROM preco_produto_fornecedor WHERE id_produto = %s'
        SQLValues = (idProduto, )
        SQLCursor.execute(SQLPrecoProdutoFornecedor, SQLValues)
        precoProduto = SQLCursor.fetchall()
        if precoProduto:
                return precoProduto[0][0]
        else:
                return "Produto não existente"

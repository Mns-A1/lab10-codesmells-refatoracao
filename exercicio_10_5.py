class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * 1.15

class ProdutoRepository:
    def salvar(self, produto: Produto):
        query = f"INSERT INTO produtos (id, nome, preco) VALUES ({produto.id_produto}, '{produto.nome}', {produto.preco});"
        print(query)

class ProdutoXMLExporter:
    def exportar(self, produto: Produto):
        return f"<produto><id>{produto.id_produto}</id><nome>{produto.nome}</nome><preco>{produto.preco}</preco></produto>"

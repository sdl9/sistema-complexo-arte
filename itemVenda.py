class ItemVenda:

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.valido = True
        self.motivo_invalido = None

        if quantidade <= 0:
            self.valido = False
            self.motivo_invalido = "Quantidade inválida."
        elif quantidade > produto.estoque:
            self.valido = False
            self.motivo_invalido = "Produto sem estoque suficiente."
        else:
            produto.estoque = produto.estoque - quantidade

            if produto.estoque == 0:
                print("Produto ficará sem estoque após compra.")

    def calcular_subtotal(self):
        return self.quantidade * self.produto.preco

    def estoque_restante(self):
        return self.produto.estoque

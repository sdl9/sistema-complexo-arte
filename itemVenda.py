class ItemVenda:

    def __init__ (self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.valido = True

        if quantidade > produto.estoque :
            print ("Produto sem estoque disponível.")
            self.valido = False
        else:
            produto.estoque = produto.estoque - quantidade
        
            if produto.estoque == 0:
                print("Produto ficará sem estoque após compra.")

    def calcular_subtotal(self):
        return self.quantidade * self.produto.preco
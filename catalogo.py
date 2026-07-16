class Catalogo:
    def __init__(self):
        self.produtos = [] # = quais produtos existem no sistema?
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto) # função propria de pegar a lista e adicionar +1 produto, que vem de (self, produto)
    
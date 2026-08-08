class Catalogo:
    def __init__(self):
        self.produtos = [] # = quais produtos existem no sistema?
    
    def adicionar_produto(self, produto):
        for produto_cadastrado in self.produtos:
            if produto_cadastrado.id_produto == produto.id_produto:
                return False
    
        self.produtos.append(produto)
        return True 

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.id_produto, "-", produto.nome, "|", "R$", produto.preco, "|", "Estoque:", produto.estoque)

    def buscar_produto_por_id(self, id_procurado):
        for produto in self.produtos:
            if produto.id_produto == id_procurado:
                return produto

        return None

        
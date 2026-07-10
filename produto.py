class Produto:

    #def init: Quando alguém criar um Produto, essa pessoa precisa informar nome e preco.
    def __init__(self, id_produto, nome, quantidade, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    #self.nome = O nome deste produto vai receber o nome que foi passado.

# class Produto        -> cria o molde
# __init__             -> define o que precisa para criar
# nome, preco          -> parâmetros recebidos
# self.nome, self.preco -> atributos guardados no objeto

#Produto          -> classe/molde
#produto          -> um objeto ou variável local
#self.produtos    -> lista de produtos dentro da venda
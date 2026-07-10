class Produto:

    #def init: Quando alguém criar um Produto, essa pessoa precisa informar nome e preco.
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    #self.nome = O nome deste produto vai receber o nome que foi passado.

# class Produto        -> cria o molde
# __init__             -> define o que precisa para criar
# nome, preco          -> parâmetros recebidos
# self.nome, self.preco -> atributos guardados no objeto
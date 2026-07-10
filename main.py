from produto import Produto
from venda import Venda

# instanciando um produto e uma venda
produto = Produto("Chopp", 18)
venda = Venda()

# adicionando o produto à venda
venda.add_produto(produto)

# printando as informações do primeiro produto da lista da venda
print(venda.produtos[0].nome)
print(venda.produtos[0].preco)
from produto import Produto
from venda import Venda

# instanciando um produto e uma venda
produto = Produto(1,"Ipa", 2, 20)
produto2 = Produto(2,"Refri", 10, 5)

venda = Venda()

# adicionando o produto à venda
venda.add_produto(produto)
venda.add_produto(produto2)

venda.resumo_venda()
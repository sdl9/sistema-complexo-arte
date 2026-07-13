from produto import Produto
from venda import Venda
from itemVenda import ItemVenda

# instanciando um produto e uma venda
produto = Produto(1,"Ipa", 2, 20)
produto2 = Produto(2,"Refri", 10, 5)

item = ItemVenda(produto, 2)
item2 = ItemVenda(produto2, 1)

venda = Venda()

# adicionando o item à venda
venda.add_item(item)
venda.add_item(item2)

venda.resumo_venda()
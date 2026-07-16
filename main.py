from produto import Produto
from venda import Venda
from itemVenda import ItemVenda

# instanciando um produto e uma venda
produto = Produto(1,"Ipa", 20, 10)
produto2 = Produto(2,"Refri", 5, 10)

item = ItemVenda(produto, 12)
item2 = ItemVenda(produto2, 11)

venda = Venda()

# adicionando o item à venda
venda.add_item(item)
venda.add_item(item2)

venda.resumo_venda()
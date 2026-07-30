from produto import Produto
from venda import Venda
from itemVenda import ItemVenda
from catalogo import Catalogo

# instanciando um produto e uma venda

produto = Produto(1,"Ipa", 20, 10)
produto2 = Produto(2,"Refri", 5, 10)

catalogo = Catalogo()

catalogo.adicionar_produto(produto)
catalogo.adicionar_produto(produto2)

produto_escolhido = catalogo.buscar_produto_por_id(2)

if produto_escolhido is None:
    print("Produto não encontrado.")
else:
    item = ItemVenda(produto_escolhido, 2)
    print(produto_escolhido.nome)

#venda = Venda()


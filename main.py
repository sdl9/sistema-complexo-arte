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

venda = Venda()

catalogo.listar_produtos()

continuar = "s"

while continuar == "s":
    id_digitado = input("Digite o ID do produto: ")
    try:
        id_escolhido = int(id_digitado)
    except ValueError:
        print("ID inválido. Digite um número de ID.")
        continue
    produto_escolhido = catalogo.buscar_produto_por_id(id_escolhido)

    if produto_escolhido is None:   
        print("Produto não encontrado.")
            
    else:
        quantidade_digitada = input("Quantidade: ")
        try:
            quantidade_escolhida = int(quantidade_digitada)
        except ValueError:
            print("Quantidade inválida. Digite um número.")
            continue

        item = ItemVenda(produto_escolhido, quantidade_escolhida)
        venda.add_item(item)

    continuar = input("Adicionar outro item? (s/n): ").lower()

venda.resumo_venda()
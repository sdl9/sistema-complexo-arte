from produto import Produto
from venda import Venda
from itemVenda import ItemVenda
from catalogo import Catalogo
from entrada import Entrada

entrada = Entrada()

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

    id_escolhido = entrada.ler_inteiro("Digite o ID do produto: ")

    produto_escolhido = catalogo.buscar_produto_por_id(id_escolhido)

    if produto_escolhido is None:   
        print("Produto não encontrado.")
        continue
       
    quantidade_escolhida = entrada.ler_inteiro("Digite a quantidade: ")

    # if quantidade_escolhida <= 0:
    #     print ("Item não adicionado.")
    #     continue

    item = ItemVenda(produto_escolhido, quantidade_escolhida)
    venda.add_item(item)

    continuar = entrada.ler_opcao("Adicionar outro item? (s/n): ")

if venda.esta_vazia():
    print ("Venda inexistente.")
else:
    venda.resumo_venda()

    while True:
        valor_pago = entrada.ler_valor("Valor pago: R$ ")
        troco = venda.calcular_troco(valor_pago)

        if troco is not None:
            break
        print("Pagamento insuficiente.")

    print ("Troco: R$", troco)
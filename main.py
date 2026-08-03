from produto import Produto
from venda import Venda
from itemVenda import ItemVenda
from catalogo import Catalogo

def ler_inteiro(mensagem):
    while True:
        valor_digitado = input(mensagem)

        try:
            return int(valor_digitado)
        except ValueError:
            print ("Digite um número válido.")

def ler_opcao(mensagem):
    while True:
        opcao = input(mensagem).lower()

        if opcao == "s" or opcao == "n":
            return opcao 

        print("Opção inválida. Digite 's' ou 'n'.")


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

    id_escolhido = ler_inteiro("Digite o ID do produto: ")

    produto_escolhido = catalogo.buscar_produto_por_id(id_escolhido)

    if produto_escolhido is None:   
        print("Produto não encontrado.")
        continue
           
    quantidade_escolhida = ler_inteiro("Digite a quantidade: ")

    item = ItemVenda(produto_escolhido, quantidade_escolhida)
    venda.add_item(item)

    continuar = ler_opcao("Adicionar outro item? (s/n): ")

venda.resumo_venda()
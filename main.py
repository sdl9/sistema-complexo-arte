from produto import Produto
from venda import Venda
from itemVenda import ItemVenda
from catalogo import Catalogo
from entrada import Entrada

entrada = Entrada()


catalogo = Catalogo()
produto2 = Produto(2,"Refri", 5, 10)

# instanciando um produto e uma venda

id_produto = entrada.ler_inteiro("ID do produto: ")
nome_produto = entrada.ler_texto("Nome do produto: ")
preco_produto = entrada.ler_valor("Preço do produto: R$ ")
estoque_produto = entrada.ler_inteiro("Estoque inicial: ")

produto = Produto(
    id_produto,
    nome_produto,
    preco_produto,
    estoque_produto
)

catalogo.adicionar_produto(produto2)
cadastro_realizado = catalogo.adicionar_produto(produto)

if not cadastro_realizado:
    print("Produto não cadastrado: ID duplicado.")

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
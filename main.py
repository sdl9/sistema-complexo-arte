from produto import Produto
from venda import Venda
from itemVenda import ItemVenda
from catalogo import Catalogo
from entrada import Entrada

entrada = Entrada()

catalogo = Catalogo()

continuar_cadastro = "s"

# cadastro de produtos

while continuar_cadastro == "s":

    id_produto = catalogo.gerar_proximo_id()
    nome_produto = entrada.ler_texto("Nome do produto: ")
    preco_produto = entrada.ler_valor("Preço do produto: R$ ")
    estoque_produto = entrada.ler_inteiro_minimo("Estoque inicial: ", 0)

    novo_produto = Produto(id_produto, nome_produto, preco_produto, estoque_produto)

    cadastro_realizado = catalogo.adicionar_produto(novo_produto)

    if cadastro_realizado:
        print("Produto cadastrado com ID:", novo_produto.id_produto)
    else:
        print("Produto não cadastrado: ID duplicado.")

    continuar_cadastro = entrada.ler_opcao("Cadastrar outro produto? (s/n): ")

catalogo.listar_produtos()

# inicio da venda

venda = Venda()

continuar_venda = "s"

while continuar_venda == "s":

    id_escolhido = entrada.ler_inteiro("Digite o ID do produto: ")

    produto_escolhido = catalogo.buscar_produto_por_id(id_escolhido)

    if produto_escolhido is None:
        print("Produto não encontrado.")
        continue

    quantidade_escolhida = entrada.ler_inteiro_minimo("Digite a quantidade: ", 1)

    novo_item = ItemVenda(produto_escolhido, quantidade_escolhida)
    venda.add_item(novo_item)

    continuar_venda = entrada.ler_opcao("Adicionar outro item? (s/n): ")

if venda.esta_vazia():
    print("Venda inexistente.")
else:
    venda.resumo_venda()

    while True:
        valor_pago = entrada.ler_valor("Valor pago: R$ ")
        troco = venda.calcular_troco(valor_pago)

        if troco is not None:
            break
        print("Pagamento insuficiente.")

    print("Troco: R$", troco)

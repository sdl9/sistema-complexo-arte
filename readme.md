# Sistema de Caixa - Status do Projeto

Sistema inicialmente simplificado. Ao longo do projeto, ficara mais complexo e completo.

## O que ja foi feito

O projeto evoluiu de um modelo simples com `Produto` e `Venda` para uma estrutura mais organizada com tres classes principais:

- `Produto`: cadastro do produto.
- `ItemVenda`: produto dentro de uma venda, com quantidade comprada.
- `Venda`: lista de itens vendidos e total da venda.

## Produto

Arquivo: `produto.py`

Representa o cadastro de um produto no sistema.

Responsabilidades atuais:

- guardar o id do produto;
- guardar o nome;
- guardar o preco;
- guardar o estoque disponivel.

Exemplo:

```python
produto = Produto(1, "Ipa", 20, 10)
```

Significa:

- id: `1`
- nome: `"Ipa"`
- preco: `20`
- estoque: `10`

## ItemVenda

Arquivo: `itemVenda.py`

Representa um produto dentro de uma venda.

Responsabilidades atuais:

- guardar qual produto esta sendo vendido;
- guardar a quantidade comprada;
- calcular o subtotal daquele item;
- verificar se ha estoque suficiente;
- descontar o estoque quando a venda e possivel;
- avisar quando nao ha estoque ou quando o estoque zera.

Exemplo:

```python
item = ItemVenda(produto, 2)
```

Significa:

- vender `2` unidades daquele produto;
- subtotal = `produto.preco * quantidade`.

## Venda

Arquivo: `venda.py`

Representa uma venda completa.

Responsabilidades atuais:

- guardar uma lista de itens vendidos;
- adicionar itens na venda;
- calcular o total da venda somando os subtotais;
- mostrar um resumo da venda.

A venda agora guarda `ItemVenda`, nao `Produto` diretamente.

Exemplo:

```python
venda.add_item(item)
```

## Main

Arquivo: `main.py`

Atualmente serve para montar o fluxo:

1. criar produtos;
2. criar itens de venda;
3. criar uma venda;
4. adicionar os itens na venda;
5. mostrar o resumo da venda.

Fluxo esperado:

```python
produto = Produto(1, "Ipa", 20, 10)
item = ItemVenda(produto, 2)

venda = Venda()
venda.add_item(item)

venda.resumo_venda()
```

## Conceitos importantes aprendidos

Antes, a venda acessava diretamente:

```python
produto.nome
```

Agora, como a venda guarda itens, o caminho e:

```python
item.produto.nome
```

Porque:

```text
item -> ItemVenda
item.produto -> Produto dentro do item
item.produto.nome -> nome do produto
```

## Proximo passo

Implementar a ideia de item valido/invalido.

Problema atual:

Mesmo quando nao ha estoque suficiente, o `ItemVenda` ainda pode ser criado e adicionado a venda.

Proxima melhoria:

No `ItemVenda`, criar um atributo:

```python
self.valido = True
```

Se nao houver estoque suficiente:

```python
self.valido = False
```

Depois, na classe `Venda`, alterar `add_item` para so adicionar itens validos:

```python
def add_item(self, item):
    if item.valido:
        self.itens.append(item)
    else:
        print("Item invalido nao foi adicionado a venda.")
```

## Depois disso

Possiveis proximos passos:

- melhorar mensagens de erro;
- impedir quantidade zero ou negativa;
- mostrar estoque restante;
- limpar comentarios antigos;
- pensar em cadastro/lista de produtos;
- futuramente permitir entrada de dados pelo usuario.

# Explicacao das Relacoes entre as Classes

Este arquivo explica como `Produto`, `Catalogo`, `ItemVenda` e `Venda` se relacionam.

## Ideia principal

As classes nao precisam sempre importar umas as outras para se relacionarem.

Muitas vezes, elas se conversam porque um objeto e criado em um lugar e depois passado para outro.

Exemplo:

```python
ipa = Produto(1, "Ipa", 20, 10)

catalogo = Catalogo()
catalogo.adicionar_produto(ipa)
```

Neste caso:

- `Produto` cria o produto `ipa`;
- `Catalogo` recebe `ipa`;
- `Catalogo` guarda `ipa` na lista `self.produtos`.

## Regra mental

```text
Se uma classe cria um objeto, ela precisa importar a classe desse objeto.
Se uma classe so recebe um objeto pronto, ela nao precisa importar.
```

Exemplo:

```python
def adicionar_produto(self, produto):
    self.produtos.append(produto)
```

Aqui o `Catalogo` nao cria um `Produto`.

Ele apenas recebe algo chamado `produto` e guarda na lista.

Por isso, neste momento, `catalogo.py` nao precisa importar `Produto`.

## Produto

`Produto` e o cadastro do produto.

Ele guarda informacoes como:

- id;
- nome;
- preco;
- estoque.

Exemplo:

```python
ipa = Produto(1, "Ipa", 20, 10)
```

Aqui `ipa` e um objeto criado a partir da classe `Produto`.

## Catalogo

`Catalogo` guarda produtos cadastrados.

Exemplo:

```python
catalogo = Catalogo()
catalogo.adicionar_produto(ipa)
```

Depois disso, o catalogo passa a ter uma lista assim:

```python
catalogo.produtos = [ipa]
```

O catalogo responde a pergunta:

```text
Quais produtos existem no sistema?
```

## ItemVenda

`ItemVenda` representa um produto dentro de uma venda.

Ele liga:

```text
produto + quantidade comprada
```

Exemplo:

```python
item_ipa = ItemVenda(ipa, 2)
```

Isso significa:

```text
vender 2 unidades do produto Ipa
```

Dentro do item:

```python
item_ipa.produto = ipa
item_ipa.quantidade = 2
```

## Venda

`Venda` guarda itens vendidos.

Exemplo:

```python
venda = Venda()
venda.add_item(item_ipa)
```

Depois disso:

```python
venda.itens = [item_ipa]
```

A venda responde a pergunta:

```text
Quais itens foram comprados nesta venda?
```

## Relacao completa

```text
Produto("Ipa")
   |
   v
ipa
   |
   v
catalogo.produtos = [ipa]
   |
   v
item_ipa.produto = ipa
   |
   v
venda.itens = [item_ipa]
```

## Por que existe `item.produto.nome`?

Antes, quando a venda guardava produtos diretamente, era possivel acessar:

```python
produto.nome
```

Agora, a venda guarda itens.

Cada item guarda um produto dentro dele.

Por isso o caminho ficou:

```python
item.produto.nome
```

Lendo da esquerda para a direita:

```text
item -> um ItemVenda
produto -> o Produto guardado dentro do item
nome -> o nome desse Produto
```

Visual:

```text
item_ipa
├── quantidade = 2
└── produto
    ├── nome = "Ipa"
    ├── preco = 20
    └── estoque = 8
```

Então:

```python
item_ipa.produto.nome
```

significa:

```text
pegue o item_ipa,
entre no produto dele,
pegue o nome desse produto.
```

## Sobre nomes parecidos

Existem varios nomes parecidos no projeto:

```python
class Produto
```

E a classe, o molde.

```python
produto = Produto(...)
```

E uma variavel que guarda um objeto `Produto`.

```python
self.produtos = []
```

E uma lista de produtos, usada no `Catalogo`.

```python
def adicionar_produto(self, produto):
```

Esse `produto` e um parametro, ou seja, o produto recebido pelo metodo.

```python
item.produto
```

E o produto guardado dentro de um `ItemVenda`.

## Sugestao para diminuir confusao

No `main.py`, em vez de usar nomes genericos:

```python
produto = Produto(1, "Ipa", 20, 10)
produto2 = Produto(2, "Refri", 5, 10)
```

Pode ser mais claro usar:

```python
ipa = Produto(1, "Ipa", 20, 10)
refri = Produto(2, "Refri", 5, 10)
```

E para os itens:

```python
item_ipa = ItemVenda(ipa, 2)
item_refri = ItemVenda(refri, 1)
```

Assim fica mais facil ler:

```python
catalogo.adicionar_produto(ipa)
venda.add_item(item_ipa)
```

## Resumo final

```text
Produto e o cadastro.
Catalogo guarda produtos.
ItemVenda usa um produto e uma quantidade.
Venda guarda itens de venda.
Entrada valida os dados digitados.
```

O `main.py` e o lugar onde as pecas sao montadas.

## Aprendizado com assert

`assert` compara o resultado real com o resultado esperado:

```python
assert venda.calcular_total() == 17
```

- sem mensagem: o teste passou;
- `AssertionError`: a expectativa estava diferente do resultado;
- com parenteses, o metodo e executado;
- cada teste precisa montar o estado que deseja verificar.

Foram testados venda vazia, subtotal, total, estoque, item invalido e troco.

## Pagamento

`Venda.calcular_troco(valor_pago)` retorna o troco ou `None` quando o pagamento e insuficiente. A classe calcula; o `main.py` decide qual mensagem mostrar.

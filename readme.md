# Sistema de Caixa em Python

Projeto didatico de um sistema de caixa executado no terminal. O objetivo e desenvolver conceitos de Python e orientacao a objetos enquanto o sistema evolui em pequenas etapas.

## Ideia do projeto

O fluxo atual representa uma venda simples:

```text
Entrada -> Catalogo -> Produto -> ItemVenda -> Venda -> Pagamento
```

- `Produto`: guarda ID, nome, preco e estoque.
- `Catalogo`: guarda, lista e busca produtos pelo ID.
- `ItemVenda`: liga um produto a uma quantidade, valida o estoque e calcula o subtotal.
- `Venda`: guarda os itens validos, calcula o total e mostra o resumo.
- `Entrada`: le e valida os dados digitados no terminal.
- `main.py`: organiza a interacao com o usuario.

## O que ja funciona

- cadastro de vários produtos pelo terminal;
- listagem do catalogo com ID, preco e estoque;
- busca de produto pelo ID;
- selecao de quantidade pelo usuario;
- validacao de entradas numericas e das opcoes `s/n`;
- inclusao de varios itens na mesma venda;
- bloqueio de quantidade zero, negativa ou maior que o estoque;
- atualizacao do estoque apos uma escolha valida;
- calculo de subtotal, total, pagamento e troco;
- bloqueio de pagamento para venda vazia;
- testes iniciais com `assert` para venda, estoque, total e troco.

## Como executar

```bash
python main.py
```

O programa mostra o catalogo, recebe os itens escolhidos e exibe o resumo quando a venda e encerrada.

## Proximos passos

1. Persistir produtos e vendas em arquivo ou banco de dados.
2. Organizar os testes em cenarios independentes.

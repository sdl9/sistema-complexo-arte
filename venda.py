class Venda:

    def __init__(self):
        self.itens = [] # = quais itens foram comprados nesta venda?

    def add_item(self, item):
        if item.valido:
            self.itens.append(item)
        else:
            print("Item não adicionado:", item.motivo_invalido)

    def calcular_total(self):
        total = 0

        for item in self.itens:
            total = total + item.calcular_subtotal()

        return total

    def calcular_troco(self, valor_pago):
        total = self.calcular_total()

        if valor_pago < total:
            return None
        
        return valor_pago - total 


    def resumo_venda(self):
        print("Produtos da venda: ")

        for numero, item in enumerate(self.itens, start=1):
            print(
                numero,
                "-",
                item.produto.nome,
                "|",
                item.quantidade,
                "x",
                "|",
                "R$",
                item.produto.preco,
                "|",
                "subtotal:",
                "R$",
                item.calcular_subtotal(),
                "|",
                "estoque restante:",
                item.estoque_restante()
            )

        print(
            "Total:",
            "R$",
            self.calcular_total()
        )

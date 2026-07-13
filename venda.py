class Venda:

    def __init__ (self):
        self.itens = []
    
    def add_item(self, item):
        self.itens.append(item)

    # Calcular total da VENDA. O 'for' fica responsável por isso.
    def calcular_total(self):
        total = 0

        # Para cada produto na lista de produtos (self.produtos), calcule o total, somando o total atual, ao subtotal (que é ref. a UM produto)
        for item in self.itens:
            total = total + item.calcular_subtotal()
        return total
    
    def resumo_venda(self):
        print ("Produtos da venda: ")

        for numero, item in enumerate (self.itens, start=1):
            print (
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
                "subtotal", 
                "R$",
                item.calcular_subtotal()
            )
        
        print (
            "Total:",
            "R$",
            self.calcular_total()
            )
class Venda:

    def __init__ (self):
        self.itens = []
    
    def add_produto(self, produto):
        self.itens.append(produto)

    # Calcular total da VENDA. O 'for' fica responsável por isso.
    def calcular_total(self):
        total = 0

        # Para cada produto na lista de produtos (self.produtos), calcule o total, somando o total atual, ao subtotal (que é ref. a UM produto)
        for item in self.itens:
            total = total + calcular_subtotal()
        return total
    
    def resumo_venda(self):
        print ("Produtos da venda: ")

        for numero, produto in enumerate (self.itens, start=1):
            print (
                numero,
                "-",
                produto.nome, 
                "|", 
                produto.quantidade,
                "x", 
                "|",
                "R$",
                produto.preco, 
                "|",
                "subtotal", 
                "R$",
                self.calcular_subtotal(produto)
            )
        
        print (
            "Total:",
            "R$",
            self.calcular_total()
            )
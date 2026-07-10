class Venda:

    def __init__ (self):
        self.produtos = []
    
    def add_produto(self, produto):
        self.produtos.append(produto)

    # Calcular subtotal do PRODUTO em si
    def calcular_subtotal(self, produto):
        subtotal = 0

        subtotal = produto.quantidade * produto.preco

        return subtotal
    
    # Calcular total da VENDA. O 'for' fica responsável por isso.
    def calcular_total(self):
        total = 0

        # Para cada produto na lista de produtos (self.produtos), calcule o total, somando o total atual, ao subtotal (que é ref. a UM produto)
        for produto in self.produtos:
            total = total + self.calcular_subtotal(produto)

        return total
    
    def resumo_venda(self):
        print ("Produtos da venda: ")

        for numero, produto in enumerate (self.produtos, start=1):
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
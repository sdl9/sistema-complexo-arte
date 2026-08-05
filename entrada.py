class Entrada:

    def ler_inteiro(self, mensagem):
        while True:
            valor_digitado = input(mensagem)

            try:
                return int(valor_digitado)
            except ValueError:
                print("Digite um número válido.")

    def ler_opcao(self, mensagem):
        while True:
            opcao = input(mensagem).lower()

            if opcao == "s" or opcao == "n":
                return opcao 

            print("Opção inválida. Digite 's' ou 'n'.")

    def ler_valor(self, mensagem):
        while True:
            valor_digitado = input(mensagem)

            try: 
                return float(valor_digitado)
            except ValueError:
                print ("Digite um valor válido.")
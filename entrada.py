class Entrada:

    def ler_inteiro(self, mensagem):
        while True:
            valor_digitado = input(mensagem)

            try:
                return int(valor_digitado)
            except ValueError:
                print("Digite um número válido.")

    def ler_inteiro_minimo(self, mensagem, minimo):
        while True:
            valor = self.ler_inteiro(mensagem)

            if valor >= minimo:
                return valor
            else:
                print("Mínimo permitido:", minimo)

    def ler_opcao(self, mensagem):
        while True:
            opcao = input(mensagem).strip().lower()

            if opcao in ("s", "n"):
                return opcao

            print("Opção inválida. Digite 's' ou 'n'.")

    def ler_valor(self, mensagem):
        while True:
            valor_digitado = input(mensagem)

            try:
                return float(valor_digitado)
            except ValueError:
                print("Digite um valor válido.")

    def ler_texto(self, mensagem):
        while True:
            texto_digitado = input(mensagem).strip()

            if not texto_digitado:
                print("Informe um nome válido")
            else:
                return texto_digitado

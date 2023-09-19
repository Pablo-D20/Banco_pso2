class Conta:
   def __init__(self, numero):
       self.numero = numero
       self.saldo = 0

   def creditar(self, valor):
       self.saldo += valor

   def debitar(self, valor):
       self.saldo -= valor

   def get_numero(self):
       return self.numero

   def set_numero(self, numero):
       self.numero = numero

   def get_saldo(self):
       return self.saldo

   def set_saldo(self, saldo):
       self.saldo = saldo


class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.creditar(self.get_saldo() * taxa)



class CriarPoupanca:
    if __name__ == '__main__':
        poupanca = ContaPoupanca("21.342-7")
        poupanca.creditar(500.87)
        poupanca.debitar(45.00)

        print(poupanca.get_saldo())

        poupanca.render_juros(0.01)
        print(poupanca.get_saldo())

        # Teste
        conta = Conta("21.342-7")
        print(type(conta))
        conta = ContaPoupanca("21.342-7")
        print(type(conta))

        conta.creditar(500.87)
        conta.debitar(45.00)

        print(conta.get_saldo())

        #teste 2
        conta = Conta("21.342-7")
        conta = ContaPoupanca(conta)
        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())

        conta.render_juros(0.01)
        print(conta.get_saldo())


class VerificaPoupanca:
    if __name__ == '__main__':
        opcao = int(input("Escolha: [1] Conta e [2] Poupanca: "))
        if opcao == 1:
            conta = Conta("21.342-7")
        else:
            conta = ContaPoupanca("21.342-7")

        conta.creditar(500.87)
        conta.debitar(45.00)

        #if isinstance(conta, ContaPoupanca):
        conta.render_juros(0.1)
        print("saldo com juros: {}".format(conta.get_saldo()))


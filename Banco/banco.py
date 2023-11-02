class ContaBancaria:
    def __init__(self, nome, tipo, numero):
        self.nome = nome
        self.saldo = 0
        self.tipo = tipo
        self.limite = 0
        self.status = False
        self.numero = numero

    def ativarLimite(self, limite):
        if self.status == False:
            print(f'Não existe uma conta ativa.')
        else:
            self.limite = limite
            print(f'Limite de {self.limite} foi ativado.')

    def verificarLimite(self):
        if self.status == False:
            print(f'Não existe uma conta ativa.')
        elif self.status and self.limite == 0:
            print(f'Você não tem limite ativo. ')
        else:
            print(f'Você possui limite ativo. Ele é de: R$ {self.limite:.2f}.')

    def sacar(self, saque):
        if self.status == False:
            print(f'Não existe uma conta ativa.')
        elif self.status and saque < self.saldo:
            self.saldo -= saque
            print(f'Saque efetuado no valor de R$ {saque:.2f}.\nSeu novo saldo é: R$ {self.saldo:.2f}')
        elif saque > self.saldo and saque <= (self.saldo + self.limite):
            self.saldo -= saque
            print(f'Saque efetuado no valor de R$ {saque:.2f}.\nSeu novo saldo é: R$ {self.saldo:.2f}')
        elif saque > self.saldo:
            print(f'O saldo não é suficiente.')

    def depositar(self, deposito):
        if self.status == False:
            print(f'Não existe uma conta ativa.')
        else:
            self.saldo += deposito
            print(f'Depósito efetuado no valor de R$ {deposito:.2f}.\nSeu novo saldo é: R$ {self.saldo:.2f}')

    def ativarConta(self):
        if self.status == False:
            self.status = True
        else:
            print(f'Conta já ativa no nome de {self.nome}.')

    def verificarSaldo(self):
        if self.status:
            print(f'Olá, {self.nome}. Seu saldo é de: R$ {self.saldo:.2f}.')
        else:
            print(f'Não existe uma conta ativa.')
class ContaBancaria():
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = saldo_inicial
    
    def depositar(self, valor):
        self.saldo_inicial += valor
        print(f'Seu novo saldo é de R${self.saldo_inicial}')
    
    def sacar(self, valor):
        if valor < self.saldo_inicial:
            novo_saldo = self.saldo_inicial - valor
            print(f'Saque de R${valor} realizado com sucesso\nSaldo atualizado R${novo_saldo}')
        else:
            print(f'Saldo Insuficiente\nSeu saldo é de R${self.saldo_inicial}')
            

saldo = ContaBancaria('joao', 0)

saldo.depositar(100)
saldo.sacar(20)
#saldo.sacar(120)
        
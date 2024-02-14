from utils import DataError
from datetime import datetime

class AgendaTransacao:
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.file_log = "Transacoes.log"

    def deposito(self, dinheiro):
        if dinheiro <= 0:
            raise DataError("O valor do depósito deve ser positivo")
        self.saldo += dinheiro
        msg = f"Depósito de {dinheiro} € realizado com sucesso. Novo saldo: {self.saldo} €"
        print(msg)
        self.registrar_transacao(msg)

    def retirar(self, dinheiro):
        if dinheiro <= 20:
            raise DataError("O valor do saque deve ser minimo 20 €")
        if dinheiro > self.saldo:
            raise DataError("Saldo insuficiente para saque.")
        self.saldo -= dinheiro
        msg = f"Saque de {dinheiro} € realizado com sucesso. Novo saldo: {self.saldo} €"
        print(msg)
        self.registrar_transacao(msg)

    def saldo_atual(self):
        print(f"Saldo atual da conta: {self.saldo} €")

    def transacao(self):
        print("---" * 15)
        print("Escolha a transação:")
        print("1. Depositar")
        print("2. Sacar")
        escolha = input("Digite o número da transação desejada (1 ou 2): ")
        if escolha == "1":
            dinheiro = float(input("Digite o valor do depósito em €: "))
            self.deposito(dinheiro)
        elif escolha == "2":
            dinheiro = float(input("Digite o valor do saque em €: "))
            self.retirar(dinheiro)
        else:
            raise DataError("Escolha inválida. Por favor, tente novamente.")

    def registrar_transacao(self, msg):
        with open("Transacoes.log", "a") as file:
            msg = f"{datetime.now()} / {msg}"
            file.write(msg + "\n")


conta = AgendaTransacao(numero_conta="123456", nome_titular="Eva", saldo=1000.0)

print("---" * 15)
conta.saldo_atual()
conta.transacao()
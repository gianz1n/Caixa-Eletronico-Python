from historico1 import Historico


class Conta:

    def __init__(self,objeto, num:str, saldo=float):
        self.titular = objeto.nome
        self.num = num
        self.saldo = saldo
        self.Historico = Historico()

    def deposito(self, valor):
        valor += self.saldo
        self.Historico.Historico.append(f'Depositou: {valor}')
        return self.saldo

    def saque(self, valor):
        if self.saldo >= valor:
           self.saldo -= valor
           self.Historico.Historico.append(f'Sacou: {valor}')
           return self.saldo 
        else: print("Saldo insuficiente!")  

    def extrato(self):
        print('='*40)
        print('Nome do titular: {self.titular}\nSaldo: {self.saldo}')
        self.Historico.Historico()


    def transfere(self, valor, destinatario):
        if valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor
            self.Historico.Historico.append(f'Transferiu R${valor} para:{destinatario.num}')
            return self.saldo
        else: print('Saldo insuficiente para realizar a transação!')

    def transfere_para(self, valor, destinatario):
        if valor <= self.saldo:
            self.saldo -= valor
            self.Historico.Historico.append(f'Transferiu R${valor} para:{destinatario.num}')
            return self.saldo
        else: print('Saldo insuficiente para realizar a transação!')

    def recebe_transferencia(self, valor, origem):
            self.saldo += valor
            self.Historico.Historico.append(f'Recebeu R${valor} da conta {origem.num}')





    
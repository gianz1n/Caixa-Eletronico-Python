from cliente import Cliente
from conta import Conta
from tkinter import *

cl1 = Cliente(nome='Gian', cpf='000.000.000-00', datanasc='03/08/2004')
c1 = Conta(cl1, num='000-1', saldo=0)


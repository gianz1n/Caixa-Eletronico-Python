from cliente import Cliente
from conta import Conta
from principal import *


while input('Deseja continuar a operação? \n') == ('S'):
    print('='*40)
    cont1 = input('1-Realizar cadastro\n2-Entrar\n')
    print('='*40)

    if cont1 == ('1'):
        cl1 = Cliente(nome=input('Nome: \n'), cpf=input('Cpf: \n'), datanasc=input('Data de nascimento: \n'))
        c1 = Conta(cl1, num=input('Número da conta: '))
        print('='*40)
    
    elif cont1 == ('2'):
        cont2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')
        print('='*40)

        while cont2 != 4:
            if cont2 == '1':
                dep = float(input('Valor a ser depositado: R$\n'))
                c1.deposito(dep)
                print('='*40)

                cont2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')
                print('='*40)

            elif cont2 == '2':
                sac = float(input('Valor a ser sacado: R$\n'))
                c1.saque(sac)
                print('='*40)

                cont2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')
                print('='*40)

            elif cont2 == '3':
                ext = float(input('Extrato da conta: \n'))
                c1.extrato(ext)
                print('='*40)

                cont2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')
                print('='*40)

            else: 
                print('Obrigado! Volte sempre')
                print('='*40)
                break
                
    





    


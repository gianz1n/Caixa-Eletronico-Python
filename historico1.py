class Historico:

    def __init__(self):
        self.Historico = []

    def historico_banco(self):
        print('Historico de transações')
        for i in self.Historico:
            print('-', i)
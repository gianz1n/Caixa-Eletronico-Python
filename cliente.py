class Cliente:

    def __init__(self, nome:str, cpf:str, datanasc:str):
        self.nome = nome
        self.cpf = cpf
        self.datanasc = datanasc

    def cliente_dados(self):
        print(f'Nome: {self.nome}\nCpf: {self.cpf}\n'
              f'Data de Nascimento: {self.datanasc}')


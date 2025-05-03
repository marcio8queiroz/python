from src.pessoa import Pessoa

# criando a subclasse PessoaFisica
class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):  
            super().__init__(nome, idade)
            self.cpf = cpf
    def apresentar(self):
        return f"ola, meu nome eh {self.get_nome()} e meu cpf é {self.cpf}"
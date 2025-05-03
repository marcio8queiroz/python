from src.pessoa import Pessoa

# criando a subclasse PessoaJuridica
class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cnpj): 
      super().__init__(nome, idade)
      self.cnpj = cnpj

    def apresentar(self):
        return f"ola, meu nome eh {self.get_nome()} e meu cnpj é {self.cnpj}"
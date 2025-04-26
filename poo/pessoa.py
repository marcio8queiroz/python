


# definição de uma classe
class Pessoa: 
    populacao = 0 

    #método construtor
    def __init__(self, nome, idade): 
        self.__nome = nome #self.nome = atributo de instancia
        self.__idade = idade #self.idade = atributo de instancia
        Pessoa.populacao = Pessoa.populacao + 1;
    
    def get_nome(self):
        return self.__nome;

    def set_nome(self, novo_nome):
       print("tamanho do novo_nome", len(novo_nome))
       if len(novo_nome) > 20:
        self.__nome = novo_nome;
       else:
           print("novo nome invalido")
    
    def get_idade(self):
        return self.__idade;

    def set_idade(self, nova_idade):
        self.__idade = nova_idade;
    
    def apresentar(self):
        return f"ola, meu nome eh {self.__nome}" 

    # criando a subclasse PessoaFisica
class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):  
            super().__init__(nome, idade)
            self.cpf = cpf
    def apresentar(self):
        return f"ola, meu nome eh {self.get_nome()} e meu cpf é {self.cpf}"
  

# criando a subclasse PessoaJuridica
class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cnpj): 
      super().__init__(nome, idade)
      self.cnpj = cnpj

    # def apresentar(self):
    #     return f"ola, meu nome eh {self.get_nome()} e meu cnpj é {self.cnpj}"



def mostrar_apresentacao(pessoa: Pessoa):
  print(pessoa.apresentar())

pf1 = PessoaFisica("Joao", 34, "123.345.475-56")
pj1 = PessoaJuridica("Empresa 1", 10, "22.455.333/0001-56")


mostrar_apresentacao(pf1)
mostrar_apresentacao(pj1)

# print(pf1.apresentar())

# pf1.set_nome("angelo marcio de queiroz motta")

# print(pj1.apresentar())

# print(dir(pf1))     

# print(dir(pf1))

# name mangling

    

# -----video aula 01 - conceitos de classe e objeto

# pessoa1 = Pessoa("Angelo", 32)
# pessoa2 = Pessoa("Henrique", 36)

# print("populacao = ", Pessoa.populacao)

# print(pessoa1.apresentar())
# print(pessoa2.apresentar())

# pessoa1.nome = "Joao"
# pessoa2.nome = "Pedro"

# print(pessoa1.apresentar())
# print(pessoa2.apresentar())

# pessoa3 = Pessoa("Nome", 45)
# print("populacao = ", Pessoa.populacao)
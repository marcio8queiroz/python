


# definição de uma classe
class Pessoa: 
    # atributos da  classe
    populacao = 0 # atributo estático
    contador = 0 # atributo estático

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

    # método de classe
    # definição: Métodos que recebem como primeiro parãmetros a classe em si (cls), 
    # permitindo manipular atributos estáticos ou criar instâncias de maneira alternativa.
    @classmethod
    def criar_anonimo(cls):
        return cls("Mario", 45)

    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1;

# método estático
# definição: Métodos que não dependem de self ou cls.
# Funcionam como funções normais dentro de uma classe, mas estão logicamente relacionados a ela.
    @staticmethod
    def validar_cpf(cpf):
        if len(cpf) < 11:
            print("CPF inválido")
        else:
            print("CPF válido")

p = Pessoa.criar_anonimo()
print(p.get_nome())

print(Pessoa.contador)
Pessoa.incrementar_contador()
print(Pessoa.contador)
Pessoa.incrementar_contador()
print(Pessoa.contador)

Pessoa.validar_cpf("123.456.78")

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
    # return f"ola, meu nome eh {self.get_nome()} e meu cnpj é {self.cnpj}"

# -----------------------------------------------------
# Diferenças entre métodos de classe, instância, etc
# -----------------------------------------------------
# Métodos de instância: operam em dados específicos de um objeto (usam self).
# Métodos de classe: operam no contexto da classe (usam cls).
# Métodos estáticos: não dependem de nenhum estado (nem self nem cls).
# Atributos estáticos: variáveis compartilhadas por todos os objetos da classe.

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
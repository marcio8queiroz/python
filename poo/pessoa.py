#definição de uma classe
class Pessoa: 
    populacao = 0 

    #método construtor
    def __init__(self, nome, idade): 
        self.nome = nome #self.nome = atributo de instancia
        self.idade = idade #self.idade = atributo de instancia
        Pessoa.populacao = Pessoa.populacao + 1;

    def apresentar(self):
        return f"ola, meu nome eh {self.nome}"

pessoa1 = Pessoa("Angelo", 32)
pessoa2 = Pessoa("Henrique", 36)

print("populacao = ", Pessoa.populacao)

print(pessoa1.apresentar())
print(pessoa2.apresentar())

pessoa1.nome = "Joao"
pessoa2.nome = "Pedro"

print(pessoa1.apresentar())
print(pessoa2.apresentar())

pessoa3 = Pessoa("Nome", 45)
print("populacao = ", Pessoa.populacao)
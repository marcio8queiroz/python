from src.pessoa import Pessoa
from src.pessoa_fisica import PessoaFisica
from src.pessoa_juridica import PessoaJuridica



def mostrar_apresentacao(pessoa: Pessoa):
  print(pessoa.apresentar())

p = Pessoa.criar_anonimo()
print(p.get_nome())

print(Pessoa.contador)
Pessoa.incrementar_contador()
print(Pessoa.contador)
Pessoa.incrementar_contador()
print(Pessoa.contador)

Pessoa.validar_cpf("123.456.78")

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
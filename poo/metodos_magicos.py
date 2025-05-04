from src.pessoa import Pessoa
from src.pessoa_fisica import PessoaFisica
from src.pessoa_juridica import PessoaJuridica

pessoa1 = Pessoa("Albert", 34)
pessoa1.adicionar_contato("email@gmail.com")
pessoa1.adicionar_contato("email@hotmail.com")
print(pessoa1)

pessoa2 = Pessoa("Eije", 36)
pessoa2.adicionar_contato("email@uol.com")
pessoa2.adicionar_contato("email@bol.com")
pessoa2.adicionar_contato("email@ig.com")
print(pessoa2)

pessoa3 = pessoa1 + pessoa2;

print(pessoa3)

# pessoa4 = pessoa1 * pessoa2;

print("-------------------------------------")

pf = PessoaFisica("Angelo", 44, "12345678910")
print(pf)

pf2 = PessoaFisica("Stephany", 23, "12345678910" )
print("A pessoa fisica 'pf é igual a pessoa fisica 'pf2'?", pf == pf2)

pj = PessoaJuridica("T2Ti", 20, "123123123123")
print(pj)

# print(dir(pf))
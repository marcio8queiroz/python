from src.pessoa import Pessoa
from src.pessoa_fisica import PessoaFisica
from src.pessoa_juridica import PessoaJuridica
from src.excecoes import CnpjInvalidoException, CpfInvalidoException

try:
 pj = PessoaJuridica("T2Ti", 12, "1231231231236")
 pj.validar_cnpj()
except CnpjInvalidoException as e:
 print(f"Ocorreu um problema: {e}")

try:
 pf = PessoaFisica("Joao", 15, "1231231236")
 pf.validar_cpf()
except CpfInvalidoException as e:
 print(f"Ocorreu um problema: {e}")
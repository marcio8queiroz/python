class CpfInvalidoException(Exception):
   def __init__(self, mensagem="CPF inválido! deve conter pelo menos 11 dígitos numéricos"):
       super().__init__(mensagem)

class CnpjInvalidoException(Exception):
   def __init__(self, mensagem="CNPJ inválido! deve conter pelo menos 14 dígitos numéricos"):
       super().__init__(mensagem)
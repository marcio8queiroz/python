import traceback
try:
    valor_informado = input("por favor, informe um número: ")
    numero_informado = int(valor_informado)
    # print(numero_informado)
    print(type(numero_informado))
    resultado = 10 / numero_informado
    
# except ValueError:
#     print("Por favor, informe um número inteiro. 01")
# except TypeError:
#     print("O programador esqueceu de fazer a conversão de tipos. 02")
    # print("deu erro")
    # print("Será que foi erro de divisao por zero?")
    # print("será que foi erro de divisao por string?" )
    # print("ocorreu um erro, estamos investigando")
# except ZeroDivisionError:
#     print("Não é possível divisão por zero!")
except Exception as e:
    print("============================================")
    print("Ocorreu uma exceção!")
    print("============================================")
    print ("Tipo: ", type(e).__name__)
    print("Mensagem: ", str(e))
    print("Traceback: ")
    trace = traceback.format_exc()
    print(trace)
else:
    print("resultado =", resultado)
finally:
    print("sempre será executado!")

# try:
#     numero = int(input("digite um valor: "))
# except ValueError:
#     print("Por favor, informe um número inteiro.")
# from calculadora import soma, subtracao, multiplicacao, divisao
from calculadora.soma import somar
from calculadora.subtracao import subtrair

v1 = 23
v2 = 54

print("variavel 01=", v1)
print("variavel 02=", v2)

print("-----------------------------------------------")
print("Operacoes da calculadora")
print("-----------------------------------------------")
print("Soma")
print("-----------------------------------------------")
print(somar(v1, v2))

print("-----------------------------------------------")
print("Subtracao")
print("-----------------------------------------------")
print(subtrair(v1, v2))



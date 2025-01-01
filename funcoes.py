def saudacao(nome="um nome qualquer"):
    print (f"olá {nome}, tudo bem?");

def operacoes(a, b):
    soma = a + b # soma - local
    diferenca = a - b # diferença - local
    return soma, diferenca

saudacao()
saudacao("EIJE")

x = 6 # variável global
y = 8 # variável global
resultado_soma, resultado_diferenca = operacoes(x, y)
print(f"A soma de {x} e {y} é: {resultado_soma}")
print(f"A diferença entre {x} e {y} é: {resultado_diferenca}")

# função para calcular a média
def calcular_media(nota_a, nota_b, nota_c):
    media = (nota_a + nota_b + nota_c) / 3 # media -> local
    return media

media_aluno = calcular_media(5, 7, 9)
print(f"A média do aluno ficou em: {media_aluno}")
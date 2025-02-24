import re

texto = "Python é divertido"
vogais = re.findall(r"[aeioué]", texto)
print(vogais)

resultado = re.search(r"Joao", texto)
print(resultado)
if resultado:
    print("encontrou")
else:
    print("não encontrou")


outro_texto = "minha string é 1234534534534-aeiou"
modificado = re.sub(r"[0-9]", "*", outro_texto)
print(modificado)

dev = "eu amo programação"
substitui = re.sub(r"[aeiou]", "*", dev)
print(substitui)

palavras = "Python é poderoso, prático e popular"
consoantes = re.findall(r"[p]", palavras)
print(consoantes)

string = "12345"
resultado = re.search(r"[abc]", string)
print(resultado)
if resultado:
    print("encontrou")
else:
    print("não encontrou")
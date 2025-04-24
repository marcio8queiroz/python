texto = "Manipulando Strings no Python!"

a = "Angelo Marcio "
b = "ANGELO MARCIO"

# Métodos de Transformação
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())

print(a.strip().lower() == b.strip().lower())

# Remoção de espaços e caracteres
frase = " oi, eu sou uma frase    "
print(frase.strip().replace("frase", "palavra"))

# Métodos de consulta
arquivo1 = "teste.txt"
arquivo2 = "teste.doc"
arquivo3 = "python.txt"

print(arquivo1, arquivo1.startswith("teste"))
print(arquivo2, arquivo2.startswith("teste"))
print(arquivo3, arquivo3.startswith("teste"))

print(arquivo1, arquivo1.endswith("txt"))
print(arquivo2, arquivo2.endswith("txt"))
print(arquivo3, arquivo3.endswith("txt"))

retorno = "Python" in texto

print("a palavra Python está dentro da variável texto?", retorno)

outro_texto = "12345a"
print(outro_texto.isdigit())
print(outro_texto.isalpha())
print(outro_texto.isalnum())

# divisão e união
frutas = "banana, laranja, pera, abacaxi"
emails = "um@gmail.com|dois@gmail.com|tres@gmail.com"

lista_frutas = frutas.replace(", ", ",").split(",")
print(lista_frutas)
print(lista_frutas[2])

lista_email = emails.split("|")
print(lista_email)

string_frutas = ', '.join(lista_frutas)
print(string_frutas)
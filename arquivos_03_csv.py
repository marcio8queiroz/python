import csv

# LEITURA DE ARQUIVOS

# lendo com listas
# with open("produto2.csv", "r") as arquivo_csv:
#     # leitor = csv.reader(arquivo_csv)
#     leitor = csv.DictReader(arquivo_csv)
#     for linha in leitor:
#         print(linha)

# lendo com dicionários
# with open("birthplace-2018-census-csv.csv", "r") as censo_csv:
#     #leitor = csv.reader(censo_csv)
#     leitor = csv.DictReader(censo_csv)
#     for linha in leitor:
#         print(linha)

# ESCRITA DE ARQUIVOS
# escrevendo com listas
# with open("produto.csv", "w") as arquivo_csv:
#     escritor = csv.writer(arquivo_csv)
#     escritor.writerow(['PRODUTO', 'QUANTIDADE', 'PRECO']) # cabeçalho
#     escritor.writerow(['CANETA', 10, 1.43])
#     escritor.writerow(['LAPIS', 120, 2.12])
#     escritor.writerow(['LIVRO', 13, 34.67])
#     escritor.writerow(['CADERNO', 68, 23.56])

# escrevendo com dicionários
# with open("produto3.csv", "w") as arquivo_csv:
#     campos = (['PRODUTO', 'QUANTIDADE', 'PRECO'])
#     escritor = csv.DictWriter(arquivo_csv, campos)
#     escritor.writeheader() #mostra o cabeçalho
#     escritor.writerow({'PRODUTO': 'PASTEL', 'QUANTIDADE': 5, 'PRECO': 12.00})
#     escritor.writerow({'PRODUTO': 'CALDO DE CANA 500ML', 'QUANTIDADE': 5, 'PRECO': 8.00})
#     escritor.writerow({'PRODUTO': 'COXINHA', 'QUANTIDADE': 1, 'PRECO': 7.00})
#     escritor.writerow({'PRODUTO': 'EMPADA', 'QUANTIDADE': 2, 'PRECO': 6.00})

# MANIPULANDO DADOS
# with open("birthplace-2018-census-csv.csv", "r") as censo_csv:
#     leitor = csv.reader(censo_csv)
#     leitor = csv.DictReader(censo_csv)
#     for linha in leitor:
#         if(int(linha['Census_night_population_count']) < 100):
#           print(f"Populacao de {linha['Birthplace']} tem menos de 100 pessoas")

# adicionando dados no final do arquivo
# escrevendo com listas
with open("produto2.csv", "a", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['BANANA', 100, 50.00])
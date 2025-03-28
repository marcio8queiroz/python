import json

# json.load = carrega de um arquivo json
# json.loads = converte de uma string json
# json.dump = salva para um arquivo json
# json.dumps = converte para uma string

with open("nfe-emissao.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)
    # print(dados)
    # print(dados.keys())
    nfeDestinatario = dados['nfeDestinatario']
    print(nfeDestinatario)
    valorTotalDaNota = dados['valorTotal']
    print(f"valor total da nota = R$ {valorTotalDaNota:.2f}")
    dados['valorTotal'] = 50000

with open("nfe-destinatario.json","w") as arquivo_destinatario:
    json.dump(nfeDestinatario, arquivo_destinatario, indent=2)

with open("nfe-emissao.json","w") as arquivo_alterado:
    json.dump(dados, arquivo_alterado, indent=2)
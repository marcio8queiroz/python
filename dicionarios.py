dic = {
    "nome": "Albert",
    "idade": 29,
    "altura": 1.75,
    "brasileiro": True,
}

print(dic)
print(f"o valor da chave 'nome' eh {dic["nome"]}")
dic["nomi"] = "pedro"
print(dic)
#print(dic["noma"])

print(dic.get("noma", "nao existe essa chave noma"))

retorno = dic.pop("nomi")
print(retorno)
print(dic)
retorno = dic.pop("nomi", "a chave nomi não existe")
print(retorno)

# del dic["idade"]
# print(dic)

for chave in dic:
 print(chave, dic[chave])
print("-------------------------------")
for chave, valor in dic.items():
 print(chave, valor)
print("-------------------------------")
for chave in dic.keys():
 print(chave, "=", dic[chave])
print("-------------------------------")
for valor in dic.values():
 print(valor)
nome = "Albert"
idade = 37
valor = 123.4567

print("Meu nome eh", nome, "e minha idade é", idade)

# f-strings
# interpolação - interpolar

print(f"Meu nome é {nome} e minha idade é {idade}")
print(f"o dobro da minha idade eh {idade * 2}")

print(f"o valor é {valor:.2f}")

# .format
print("----------------------------")
print("usando o .format")
print("----------------------------")
print("Meu nome é {nn} e minha idade é {ii}".format(nn=nome, ii=idade))

print("o valor é {:.2f}".format(valor))

# usando o % - desencorajado
print("----------------------------")
print("usando o %")
print("----------------------------")
print("Meu nome é %s e minha idade é %d" % (nome, idade)) 
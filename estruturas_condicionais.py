nome = "Abert" 
idade = 15
altura = 1.75 
eh_estudante = True 

if idade != altura:
    print("idade diferente de altura")
else:
   print("idade igual a altura")

if idade < 16:
   print("nao pode votar")
elif idade < 18 or idade >= 65:
   print("voto facultativo")

 
else: 
   print("voto obrigatório")

if idade >= 18:
   print("adulto")
# print("esse será sempre impresso")
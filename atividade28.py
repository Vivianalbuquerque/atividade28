from datetime import date 
today = date.today()
anoatual = today.year
maior = []
menor = []
for i in range(7):
    anonascimento = int(input("digite o seu ano de nascimento "))
    if anoatual - anonascimento >= 18 :
        maior.append (anonascimento)
    else: 
        menor.append(anonascimento)
print(maior)
print(menor)
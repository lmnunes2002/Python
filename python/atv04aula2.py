import os
os.system("cls||clear")

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 65:
    print("Seu voto é obrigatório.")
elif idade >= 16 or idade >= 65:
    print("Seu voto é opcional.") 
else:
    print("Você não tem idade para votar.")  
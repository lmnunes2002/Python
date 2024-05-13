import os
os.system("cls||clear")

numero = int(input("Digite o número desejado: "))

while numero < 0 or numero > 10:
    numero = int(input("Digite o número novamente: "))

print(f"Esse é seu número: {numero}")
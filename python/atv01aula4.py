import os
os.system("cls||clear")

numero = float(input("Digite a nota desejado: "))

while numero < 0 or numero > 10:
    numero = float(input("Digite a nota novamente: "))

print(f"Esse é seu número: {numero}")
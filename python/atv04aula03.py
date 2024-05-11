import os
os.system("cls||clear")

inteiro = int(input("Digite a tabuda desejada: "))

print(f"Tabuade de {inteiro}")
for i in range(1,11):
    print(f"{inteiro}*{i} = {inteiro * i}")
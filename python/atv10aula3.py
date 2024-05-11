import os
os.system("cls||clear")

soma = 0

for i in range(1,4):
    nota = int(input("Digite sua {i}ª nota: "))

    soma += nota

media = soma / 3

if media <= 7:
    print("Aprovado")
elif media >= 6:
    print("Recuperação")
else:
    print("Reprovado")
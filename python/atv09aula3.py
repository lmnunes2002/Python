import os
os.system("cls||clear")

soma = 0
media = 0

for i in range(1, 5):
    num = int(input(f"Digite a {i}º nota: "))
    
    soma += num

media = soma / 4

print(f"A média do aluno é: {media}")
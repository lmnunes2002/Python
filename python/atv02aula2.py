import os
os.system("cls||clear")

inteiro_um = int(input("Digite o primeiro número: "))
inteiro_dois = int(input("Digite o segundo número: "))

print(f"Soma: {(inteiro_um + inteiro_dois)}")
print(f"Média: {(inteiro_um + inteiro_dois) / 2}")
print(f"Produto: {(inteiro_um * inteiro_dois)}")

if inteiro_um > inteiro_dois:
    print(f"Maior número: {inteiro_um}")
    print(f"Menor número: {inteiro_dois}")
elif inteiro_dois > inteiro_um:
    print(f"Maior número: {inteiro_dois}")
    print(f"Menor número: {inteiro_um}")
elif inteiro_um == inteiro_dois:
    print("Os números são iguais")
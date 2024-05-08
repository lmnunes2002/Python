import os
os.system("cls||clear")

nota = float(input("Digite sua nota: "))

if nota >= 7.0:
    print("Você foi aprovado")
elif nota >= 5.0:
    print("Recuperação")
else:
    print("Reprovado")

print("===== FIM =====")
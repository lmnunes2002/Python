import os
os.system("cls||clear")

A = int(input("Digite o 1º inteiro: "))
B = int(input("Digite o 2º inteiro: "))
op = input("Digite a operação desejada: ")

match(op):
    case '+':
        print(f"O resultado é {A + B}")
    case '-':
        print(f"O resultado é {A - B}")
    case '*':
        print(f"O resultado é {A * B}")
    case '/':
        print(f"O resultado é {A / B}")
# Python
switchcase:
 import os
 os.system("cls||clear")

 opcao = int(input("Digite a opção desejada: "))

 match(opcao):
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opçaõ 3")
    case 4:
        print("Opção 4")
    case _:
        print("Default")

laço for:
    for i in range(1,11):
        print(f"Número {i}")

    for i in range (10,0,-1):
        print(f"Número {i}")
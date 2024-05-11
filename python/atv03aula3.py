import os
os.system("cls||clear")

sexo = input("Digite seu sexo (M ou F): ")
estado_civil = input("Digite seu estado civil: ")

sexo = sexo.upper()
estado_civil = estado_civil.upper()

match(sexo):
    case 'M':
        print(f"Sexo: {sexo}")
        print(f"estado civil: {estado_civil}")
    case 'F':
        if estado_civil == "CASADA":
            anos_casamento = input("Digite seus anos de casamento: ")
            print(f"Sexo: {sexo}")
            print(f"Estado civil: {estado_civil}")
            print(f"Anos de casamento: {anos_casamento}")
        else:
            print(f"Sexo: {sexo}")
            print(f"Estado civil: {estado_civil}")
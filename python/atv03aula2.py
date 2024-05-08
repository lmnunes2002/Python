import os
os.system("cls||clear")

login = input("Cadastre seu login: ")
senha = input("Cadastre sua senha: ")

login_verdadeiro = input("Digite seu login: ")
senha_verdadeiro = input("Digite sua senha: ")

if login == login_verdadeiro:
    print("Bem vindo")
else:
    print("Login ou senha inválidos")
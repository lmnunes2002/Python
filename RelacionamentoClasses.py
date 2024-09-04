# import os

# # Limpa o terminal.
# os.system("cls||clear")

# # Criando a classe Endereço.
# class Endereco:
#     # Criando um constutor.
#     def __init__(self, logradouro: str, numero: str) -> None:
#         self.logradouro = logradouro
#         self.numero = numero

#     # Semelhante ao toString()
#     def __str__(self) -> str:
#         return (
#             f"\nLogradouro: {self.logradouro}" 
#             f"\nNúmero: {self.numero}"
#         )

# # Criando a classe Aluno.
# class Aluno:
#     # Criando um construtor.
#     def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
#         self.nome = nome
#         self.idade = idade
#         self.endereco = endereco
    
#     # Semelhante ao toString()
#     def __str__(self) -> str:
#         return (
#             f"Nome: {self.nome}" 
#             f"\nIdade: {self.idade}"
#             f"\n\nEndereço: {self.endereco}"
#         )

# # Instanciando classe.
# endereco1 = Endereco("Rua A", "33")
# aluno1 = Aluno("Marta", 22 , endereco1)

# print(aluno1)
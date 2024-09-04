import os

# Limpa o terminal.
os.system("cls||clear")

# Criando a classe Pet
class Pet:
    # Criando um construtor com valores padrão
    def __init__(self, nome: str = "", idade: int = 0, raca: str = "", porte: str = "", alimentacao: str = "") -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

    # Criando um método para solicitar dados
    def solicitar_dados(self) -> None:
        self.nome = input("Digite o nome do pet: ")
        self.idade = int(input("Digite a idade do pet: "))
        self.raca = input("Digite a raça do pet: ")
        self.porte = input("Digite o porte do pet: ")
        self.alimentacao = input("Digite a alimentação do pet: ")

    # Criando um método para representação como string
    def __str__(self) -> str:
        return (f"Nome: {self.nome}\n"
                f"Idade: {self.idade}\n"
                f"Raça: {self.raca}\n"
                f"Porte: {self.porte}\n"
                f"Alimentação: {self.alimentacao}")

# Instanciando o objeto Pet sem parâmetros
pet = Pet()

# Solicitando dados ao usuário
pet.solicitar_dados()

# Exibindo os dados do pet
print(pet)

# import os

# # Limpa o terminal.
# os.system("cls||clear")

# # Criando a classe Pet
# class Pet:
#     #Criando um construtor
#     def __init__(self, nome: str, idade: int, raca: str, porte: str, alimentacao: str) -> None:
#         self.nome = nome
#         self.idade = idade
#         self.raca = raca
#         self.porte = porte
#         self.alimentacao = alimentacao

#     # Criando um método
#     def solicitar_dados(self) -> None:
#         self.Nome = input("Digite o nome do pet: ")
#         self.idade = int(input("Digite a idade do pet: "))
#         self.raca = input("Digite a raça do pet: ")
#         self.porte = input("Digite o porte do pet: ")
#         self.alimentacao = input("Digite a alimentação do pet: ")

#     # Criando um método
#     def __str__(self) -> str:
#         return {
#             f"Nome: {self.nome}" 
#             f"\nIdade: {self.idade}" 
#             f"\nRaça: {self.raca}" 
#             f"\nPorte: {self.porte}" 
#             f"\nAlimentação: {self.alimentacao}"
#         }

# # Exibindo os atributos um por um
# # print(pet.nome)
# # print(pet.idade)
# # print(pet.raca)
# # print(pet.porte)
# # print(pet.alimentacao)

# # Instanciando o objeto
# pet = Pet()

# pet = Pet.solicitar_dados()

# # Exibindo o método
# print(pet.exibir_dados())
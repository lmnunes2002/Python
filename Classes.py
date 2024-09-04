import os

# Limpa o terminal.
os.system("cls||clear")

# Criando a classe Aluno.
class Aluno:
    # Criando um construtor
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    # Criando um método
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"

# Instanciando classe
aluno = Aluno("Marta", 22)

# Exibindo os atributos um por um
# print(aluno.nome)
# print(aluno.idade)

# Exibindo o método
print(aluno.exibir_dados())
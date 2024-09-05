# Importando Enum.
from enum import Enum
import os

# Limpando o terminal.
os.system("cls||clear")

# Criando o Enum.
class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

# Criando classe Aluno.
class Aluno:
    # Criando um construtor.
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    # Semelhante ao toString().
    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
        )
    
# Instanciando classes.
aluno_1 = Aluno("Marta", 22, Sexo.FEMININO)

# Exibindo dados.
print(aluno_1)
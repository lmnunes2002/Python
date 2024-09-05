# Importando enum.
from enum import Enum
import os

# Limpando o terminal.
os.system("cls||clear")

# Criando o Enum.
class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

# Aplicação.
print(f"Sexo: {Sexo.FEMININO}")
print(f"Sexo: {Sexo.FEMININO.name}")
print(f"Sexo: {Sexo.FEMININO.value}")
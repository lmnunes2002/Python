# importando Enum.
from enum import Enum
import os

# Limpando o temrinal.
os.system("cls||clear")

# Criando os Enums.
class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

# Crinado a classe funcionario.
class Funcionario:
    # Criando o construtor.
    def __init__(self, nome: str, id: str, salario: float, setor: Setor, sexo: Sexo, idade: int) -> None:
        self.nome = nome
        self.id = id
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
        self.idade = idade

    # Semelhante ao toString().
    def __str__(self) -> str:
        return(
            f"Nome: {self.nome}"
            f"\nID: {self.id}"
            f"\nSalário: {self.salario}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
            f"\nIdade: {self.idade}"
        )
    
# Instanciando classes.
funcionario_1 = Funcionario("Lucas", "123456", 4000, Setor.FINANCEIRO, Sexo.MASCULINO, 22)

# Exibindo dados.
print(funcionario_1)
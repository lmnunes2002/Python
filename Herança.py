# Importando metodos abstratos.
from abc import ABC, abstractmethod
import os

# Limpando terminal.
os.system("cls||clear")

# Criando a classe Funcionario.
class Funcionario(ABC):
    # Criando o construtor.
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    # Decorador.
    # Criando um método abstrato.
    @abstractmethod
    def salario_final(self) -> float:
        pass

    # Semelhante ao toString().    
    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"\nSalário: {self.salario}"
            f"\nSalário final: {self.salario_final()}"
            )

# Criando a classe Motoboy.   
class Motoboy(Funcionario):
    # Acréscimo de 10%.
    BONIFICACAO = 1.1

    # Método de salário final.
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

# Criando a classe Engenheiro.
class Engenheiro(Funcionario):
    BONIFICACAO = 1.2
    # Criando o construtor.
    def __init__(self, nome: str, salario: float, crea: str) -> None:
        super().__init__(nome, salario)
        self.crea = crea

    # Método de salário final.
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\nCrea: {self.crea}"
        )

# Instanciando classes.
motoboy_1 = Motoboy("José", 1000)
engenheiro_1 = Engenheiro("Marta", 1000, "4652132")

# Exibindo os dados do motoboy.
print(motoboy_1)
print(engenheiro_1)
# Importando metódos abstratos.
from abc import ABC, abstractmethod
import os

# Limpando o terminal.
os.system("cls||clear")

# Criando a classe Endereco.
class Endereco:
    # Criando o construtor.
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    # Semelhante ao toString().
    def __str__(self) -> str:
        return (
            f"Logradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
        )
    
#  Criando a classe Funcionario.
class Funcionario(ABC):
    # Criando o construtor.
    def __init__(self,  nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.endereco = endereco

    # Decorador.
    # Criando um metódo abstrato.
    @ abstractmethod
    def salario_final(self) -> float:
        pass

    # Semelhante ao toString().
    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nSalário: {self.salario}"
            f"\nSalário final: {self.salario_final()}"
            f"\nEndereço: {self.endereco}"
        )

# Criando a classe Engenheiro.
class Engenheiro(Funcionario):
    BONIFICACAO = 1.1
    # Criando o construtor.
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = crea

    # Método de salário final.
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
    # Semelhante ao toString().
    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\nCrea: {self.crea}"
        )

# Criando a classe Médico:
class Medico(Funcionario):
    BONIFICACAO = 1.2
    # Criando o construtor.
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = crm

    # Método de salário final.
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
    # Semelhante ao toString().
    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\nCrea: {self.crm}"
        )
    
# Instanciando classes.
endereco_1 = Endereco("Rua A", "33", "Do lado do posto", "12345", "Salvador")
engenheiro_1 = Engenheiro("Marta", "1234-5678", "marta@email", 8000, endereco_1, "CREA-123")

endereco_2 = Endereco("Rua B", "17", "Perto da UPA", "67890", "Feira de Santana")
medico_1 = Medico("João", "8765-4321", "joao@email", 9000, endereco_2, "CRM-456")

# Exibindo dados.
print(engenheiro_1)
print(medico_1)
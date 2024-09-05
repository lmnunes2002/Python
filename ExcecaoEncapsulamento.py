import os

# Limpando o terminal.
os.system("cls||clear")

# Criando a classe conta.
class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 100 # Atributo Protegido.

    # Semelhante ao getSaldo()
    # def get_saldo(self):
    #   return self._saldo

    # Decorador.
    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor: float):
        self._saldo -- valor
        return self._saldo
    
    def depositar(self, valor: float):
        self._saldo += valor
        return self._saldo

# Criando a classe conta corrente.
class ContaCorrente(Conta):
    pass

# Criando a classe conta poupança.
class ContaPoupanca(Conta):
    pass

# Instanciando as classes.
conta_corrente = ContaCorrente(222, 333)

# Exibindo dados.
print(f"Número da conta: {conta_corrente.numero_conta}")
print(f"Saldo: {conta_corrente.saldo}")
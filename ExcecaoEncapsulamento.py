import os

# Limpando o terminal.
os.system("cls||clear")

# Criando minha propria exceção.
class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

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
    
    def sacar(self) -> str:
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        try:
            self.__verificar_sacar(valor_saque)
            self.__verificar_valor_negativo(valor_saque)
        except (SaldoInsuficienteError, ValorNegativoError) as erro:
            return f"Prezado cliente, erro: {erro}"
    
        return f"Saque realizado com sucesso"
    
    # Método privado 1.
    def __verificar_sacar(self, valor_saque) -> None:
        if valor_saque > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        
        self._saldo -= valor_saque

    # Método privado 2.
    def __verificar_valor_negativo(self, valor_deposito):
        if valor_deposito < 0:
            raise ValorNegativoError("Valor negativo.")
    
    def depositar(self):
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        try:
            self.__verificar_valor_negativo(valor_deposito)
        except ValorNegativoError as erro:
            return f"Prezado cliente, erro: {erro}"
    
        self._saldo += valor_deposito
        return f"Depósito realizado com sucesso"

# Criando a classe conta corrente.
class ContaCorrente(Conta):
    pass

# Criando a classe conta poupança.
class ContaPoupanca(Conta):
    pass

# Instanciando as classes.
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

# Exibindo dados.
print(f"Número da conta: {conta_corrente.numero_conta}")
print(f"Saldo: {conta_corrente.saldo}")

# Sacar com saldo insuficiente.
print("\nConta corrente: ")
print(conta_corrente.sacar())
print(f"Saldo: {conta_corrente.saldo}")

print("\nConta poupança: ")
print(conta_poupanca.sacar())
print(f"Saldo: {conta_poupanca.saldo}")

print("\nDepositar: ")
print(conta_poupanca.depositar())
print(conta_poupanca.saldo)
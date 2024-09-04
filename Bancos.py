import os

# Limpa o terminal 
os.system("cls||clear")

# Criando classe conta bancária.
class Conta_Bancaria:
    # Criando um construtor.
    def __init__(self, banco: str, agencia: str, numero_conta: str, tipo_conta: str, saldo_atual: float, limite: float) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo_atual = saldo_atual
        self.limite = limite

    # Semelhanto ao toString()
    def __str__(self) -> str:
        return (
            f"\nBanco: {self.banco}"
            f"\nAgência: {self.agencia}"
            f"\nNúmero da conta: {self.numero_conta}"
            f"\nTipo da conta: {self.tipo_conta}"
            f"\nSaldo atual: {self.saldo_atual}"
            f"\nLimite dispónivel: {self.limite}"
        )
    
# Criando classe funcionário.
class Funcionario:
    #Criando um construtor.
    def __init__(self, codigo_funcionario: str, nome: str, endereco: str, telefone: str, email: str, conta_banco: Conta_Bancaria) -> None:
        self.codigo_funcionario = codigo_funcionario
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.conta_banco = conta_banco
    
    # Semelhante ao toString().
    def __str__(self) -> str:
        return(
            f"Código do Funcionário: {self.codigo_funcionario}"
            f"\nNome: {self.nome}"
            f"\nEndereço: {self.endereco}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\n\nConta banco: {self.conta_banco}"
        )

# Instanciando classes
conta1 = Conta_Bancaria("Santander", "Brotas", "12345", "Corrente", 20000.00, 1000.0)
funcionario1 = Funcionario("260602", "Lucas", "Rua A", "1234-5678", "lucas@email", conta1)

# Exibindo dados
print(funcionario1)
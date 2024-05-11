import os 
os.system("cls||clear")

print("\n=== Solicitando dados ===")
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o valor do produto: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))

if quantidade_produto <= 5:
    desconto = 0.02
elif quantidade_produto <= 10:
    desconto = 0.03
else:
    desconto = 0.05

sub_total = preco_produto * quantidade_produto
total_pagar = sub_total - (sub_total * desconto)

print("\n=== Exibindo resultados ===")
print(f"\nNome do produto: {nome_produto}")
print(f"\nPreço do produto: {preco_produto}")
print(f"\nQuantidade do produto: {quantidade_produto}")
print(f"\nTotal a pagar: {total_pagar}")

print("\n==== Fim ====")

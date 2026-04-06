print("=== SISTEMA DE CAIXA ===")

nome_cliente = input("Digite o nome do cliente: ")
total_compra = 0
continuar = "s"

while continuar.lower() == "s":
    valor_produto = float(input("Digite o valor do produto: R$ "))
    total_compra += valor_produto
    continuar = input("Deseja passar mais um produto? (s/n): ")

print("\n" + "="*25)
print(f"Cliente: {nome_cliente}")
print(f"Total a pagar: R$ {total_compra:.2f}")
print("="*25)

# --- Calculadora de Grana do Vendedor ---

nome = input("Quem é o vendedor? ")
cpf = input("Qual o CPF dele? ")

# Deixando o cargo e matrícula fixos pra facilitar
cargo = "Vendedor Sênior"
matricula = "MAT-2024-001"

# Entradas dos valores
salario = float(input("Quanto ele ganha de base? R$ "))
vendas = int(input("Quantos carros ele vendeu esse mês? "))
comissao_por_carro = float(input("Qual a % de comissão? "))
transporte = float(input("Valor do VT: R$ "))
comida = float(input("Valor do VA: R$ "))

# Fazendo as contas
# Calcula a porcentagem em cima do salário e multiplica pelas vendas
total_comissao = (salario * (comissao_por_carro / 100)) * vendas
bolada_final = salario + total_comissao + transporte + comida

# Mostrando o resultado de um jeito simples
print("\n--- FOLHA DE PAGAMENTO ---")
print(f"Funcionário: {nome}")
print(f"Cargo: {cargo} (Matrícula: {matricula})")
print(f"Salário: R$ {salario:.2f}")
print(f"Comissão total: R$ {total_comissao:.2f}")
print(f"Benefícios (VT+VA): R$ {transporte + comida:.2f}")
print("-" * 30)
print(f"TOTAL QUE VAI CAIR NA CONTA: R$ {bolada_final:.2f}")
print("--------------------------")

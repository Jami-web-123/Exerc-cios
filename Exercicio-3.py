produto = input("Nome do produto: ")
descricao = input("Descrição: ")
quantidade = int(input("Quantidade inicial: "))
valor_unitario = float(input("Valor unitário: R$ "))

while True:
    valor_total = quantidade * valor_unitario
    print("\n--- INFORMAÇÕES DO ESTOQUE ---")
    print(f"Produto: {produto} | Descrição: {descricao}")
    print(f"Qtd: {quantidade} | Unidade: R$ {valor_unitario:.2f}")
    print(f"VALOR TOTAL EM ESTOQUE: R$ {valor_total:.2f}")
    
    print("\nO que deseja atualizar?")
    print("1- Nome | 2- Descrição | 3- Quantidade | 4- Valor Unitário | 5- Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        produto = input("Novo nome: ")
    elif opcao == '2':
        descricao = input("Nova descrição: ")
    elif opcao == '3':
        quantidade = int(input("Nova quantidade: "))
    elif opcao == '4':
        valor_unitario = float(input("Novo valor unitário: R$ "))
    elif opcao == '5':
        break
    else:
        print("Opção inválida!")

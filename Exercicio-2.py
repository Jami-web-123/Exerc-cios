print("=== Sistema de Notas ===")
nome = input("Nome do aluno: ")
turma = input("Turma: ")
materia = input("Matéria: ")

soma_notas = 0
quantidade = 0
continuar = 's'

while continuar.lower() == 's':
    nota = float(input(f"Digite a {quantidade + 1}ª nota: "))
    soma_notas += nota
    quantidade += 1
    continuar = input("Deseja inserir mais uma nota? (s/n): ")

if quantidade > 0:
    media = soma_notas / quantidade
    print(f"\nAluno: {nome} | Turma: {turma} | Matéria: {materia}")
    print(f"Média Final: {media:.2f}")

    if media >= 7:
        print("Status: APROVADO!")
    elif 5 <= media < 7:
        print("Status: EM EXAME.")
    else:
        print("Status: REPROVADO. ")

alunos = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(",")

for i in range(0, len(alunos), 3):
    nome, idade, nota = alunos[i], int(alunos[i + 1]), float(alunos[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")
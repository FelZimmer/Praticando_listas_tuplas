notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
notas = [float(i) for i in notas]
media = sum(notas) / len(notas)

print(f"Média final da turma: {media:.2f}")
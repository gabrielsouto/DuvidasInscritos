alunos = {}

quantidade_alunos = int(input("Digite a quantidade de alunos:"))

for i in range(1, quantidade_alunos+1):
    nome = input("Digite o nome do " + str(i) + "º aluno:")
    notas = []
    for posicao_nota in range(0, 4):
        notas.append(round(float(input("Digite a " + str(posicao_nota+1) + "ª nota do aluno " + nome + ":")), 1))
    alunos[nome] = notas

print("\nNotas dos alunos")
print("- " * 9)

for aluno in alunos.items():
    media = round(sum(aluno[1])/4 , 1)
    
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(aluno[0].ljust(15), end=" ")
    print(str(aluno[1][0]).ljust(4), end=" ")
    print(str(aluno[1][1]).ljust(4), end=" ")
    print(str(aluno[1][2]).ljust(4), end=" ")
    print(str(aluno[1][3]).ljust(4), end=" ")
    print(str(media).ljust(4), end=" ")
    print(situacao.rjust(10))

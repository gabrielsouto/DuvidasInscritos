notas = []
for posicao_nota in range(4):
    notas.append(round(float(input("Digite a " + str(posicao_nota+1) + "ª nota do aluno :")), 2))

print("\nSituação do aluno")
print("- " * 8)

media_anual = round(sum(notas)/4 , 2)

if media_anual >= 7:
    situacao = "Aprovado"
elif media_anual >= 5 and media_anual < 7:
    prova_recuperacao = round((50 - 4 * media_anual) / 6, 2)
    situacao = f"Deve tirar {prova_recuperacao} na prova de recuperação"
else:
    situacao = "Reprovado"

print("Média: " + str(media_anual).ljust(4), end=" ")
print(situacao.rjust(10))

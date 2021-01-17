# 01. Você acaba de comer em um restaurante, e recebeu a seguinte conta:
# R$44.50 de custo da refeição, a ser acrescido de 6.75% de impostos e 15% de
# gorjeta. Implemente um programa que calcule a gorjeta com base no custo total
# da refeição (incluindo impostos).
custo_refeicao = 44.5
porcentagem_impostos = 6.75
porcentagem_gorjeta = 15

valor_impostos = round(custo_refeicao * porcentagem_impostos / 100, 2)
custo_total_refeicao = round(custo_refeicao + valor_impostos, 2)

valor_gorjeta = round(custo_total_refeicao * porcentagem_gorjeta / 100, 2)

valor_total = custo_total_refeicao + valor_gorjeta

print("Custo da refeição: R$", custo_refeicao)
print("Porcentagem de impostos sobre o custo da refeição:", porcentagem_impostos, "%")
print("Valor dos impostos: R$", valor_impostos)
print("Custo total da refeição (custo da refeição + impostos): R$", custo_total_refeicao)
print("Valor da gorjeta: R$", valor_gorjeta)
print("Valor total da refeição (custo da refeição + impostos + gorjeta): R$", valor_total)

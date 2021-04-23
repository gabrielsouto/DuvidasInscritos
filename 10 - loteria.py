#Set é uma coleção não ordenada e não indexada. Não permite valores duplicados.
sorteadas = set()
apostadas = set()
premios = {3: "terno", 4: "quadra", 5: "quina", 6: "sena"}
   
while len(apostadas) < 6:
    apostadas_digitadas = set(map(int, (input().split())))
    apostadas = {apostada_digitada for apostada_digitada in apostadas_digitadas if 1 <= apostada_digitada <= 99}

while len(sorteadas) < 6:
    sorteadas_digitadas = set(map(int, (input().split())))
    sorteadas = {sorteada_digitada for sorteada_digitada in sorteadas_digitadas if 1 <= sorteada_digitada <= 99}

acertadas = apostadas.intersection(sorteadas)

if len(acertadas) >= 3:
    print(premios[len(acertadas)])
else:
    print("azar")

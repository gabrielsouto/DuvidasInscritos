def calc_soma(a: list, b: list) -> list:
    matriz_3 = []
    
    for y in range(4):
        matriz_3.append([])
        for x in range(4):
            matriz_3[y].append(a[y][x] + b[y][x])
    
    return matriz_3

matrizes = {"matriz_1": [], "matriz_2": []}

for matriz_posicao in range(1, 3):
    for linha in range(4):
        matrizes[f"matriz_{matriz_posicao}"].append([])
        
        while len(matrizes[f"matriz_{matriz_posicao}"][linha]) < 4:
            numero_digitado = int(input(f"Digite o {len(matrizes[f'matriz_{matriz_posicao}'][linha])+1}º número da {linha+1}ª linha da {matriz_posicao}ª matriz: "))
            if numero_digitado >= 0:
                matrizes[f"matriz_{matriz_posicao}"][linha].append(numero_digitado)
            else:
                print("Número negativo, saindo do programa.")
                exit()

resultado = calc_soma(matrizes["matriz_1"], matrizes["matriz_2"])

print(resultado)

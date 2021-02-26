# 2-Faça uma função que receba uma lista de números inteiros (preenchida pelo usuário), calcule o quadrado de cada número e retorne essa nova lista.
lista_entrada = []
#lista_quadrado = []

'''
while True:
    entrada = input("Digite um número inteiro ou qualquer outra coisa para sair (inclusive Enter):")
    if entrada.isdigit():
        lista_entrada.append(int(entrada))
    else:
        break
'''
def ler_inteiros():  
    while True:
        entrada = input("Digite um número inteiro ou qualquer outra coisa para sair (inclusive Enter):")
        try:
            int(entrada)
        except ValueError:
            break
        else:
            lista_entrada.append(int(entrada))
    return lista_entrada

ler_inteiros()

if len(lista_entrada) > 0:
    print(lista_entrada)
    
    #for i in lista_entrada:
    #    lista_quadrado.append(i**2)
        
    lista_quadrado = list(map(lambda x:x**2, lista_entrada))
        
    print(lista_quadrado)
    
else:
    print("Nenhum número inteiro foi informado.")

def valida_range(codigo):
    if codigo < 10000 or codigo > 30000:
        return False
    else:
        return True
    
def retorna_digito_verificador(codigo_valido):
    soma_das_multiplicacoes = 0
    
    #peso dos digitos
    peso_dos_digitos = [2, 3, 4, 5, 6]
    
    #separar os digitos
    digitos = [int(x) for x in str(codigo_valido)]
    
    #soma da multiplicacao dos digitos pelos pesos
    for posicao in range(0,5):
        soma_das_multiplicacoes += digitos[posicao] * peso_dos_digitos[posicao]
    
    digito_verificador = soma_das_multiplicacoes % 7
    
    return digito_verificador


codigo_produto = int(input('Digite o código do produto: '))

while valida_range(codigo_produto) == False:
    codigo_produto = int(input('Digite um valor entre 10000 e 30000: '))
    
digito = retorna_digito_verificador(codigo_produto)    
print("O código com dígito é:", str(codigo_produto), "-", str(digito), sep="")

nome_arquivo = input("Digite o nome do arquivo:")
while nome_arquivo != nome_arquivo.lower() or nome_arquivo[len(nome_arquivo)-4:len(nome_arquivo)].lower() != ".txt" or not nome_arquivo.replace(".txt", "").isalpha():
    nome_arquivo = input("Nome inválido, digite o nome do arquivo apenas com letras, em minúsculo e com extensão .txt:")    

nome_sem_extensao = list(nome_arquivo.replace(".txt", ""))

letras = list(map(chr, range(ord('a'), ord('z')+1)))
numeros = list(range(1, len(letras)+1))
dicionario = dict(zip(letras, numeros))

def criptografa(nome_arquivo, dicionario_equivalencias):
    posicao_letra, letra = next(((indice, valor) for indice, valor in enumerate(nome_arquivo) if str(valor).isalpha()), (None, None))
    
    if posicao_letra is not None and letra is not None:
        nome_arquivo[posicao_letra] = str(dicionario_equivalencias[letra])
        return criptografa(nome_arquivo, dicionario_equivalencias)
    else:
        return nome_arquivo
        
nome_sem_extensao_criptografado = criptografa(nome_sem_extensao, dicionario)
print("_".join(nome_sem_extensao_criptografado) + ".juice")

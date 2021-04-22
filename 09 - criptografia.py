nome_arquivo = input("Digite o nome do arquivo:")
while nome_arquivo != nome_arquivo.lower() or nome_arquivo[len(nome_arquivo)-4:len(nome_arquivo)].lower() != ".txt" or not nome_arquivo.replace(".txt", "").isalpha():
    nome_arquivo = input("Nome inválido, digite o nome do arquivo apenas com letras, em minúsculo e com extensão .txt:")    

nome_sem_extensao = nome_arquivo.replace(".txt", "")

letras = list(map(chr, range(ord('a'), ord('z')+1)))
numeros = list(range(1, len(letras)+1))
dicionario = dict(zip(letras, numeros))

nome_sem_extensao_criptografado = [str(dicionario[letra]) for letra in nome_sem_extensao]
print("_".join(nome_sem_extensao_criptografado) + ".juice")

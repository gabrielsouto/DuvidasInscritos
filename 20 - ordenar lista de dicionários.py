lista = []

def cadastra_produto(produto_para_cadastrar: dict):
    lista.append(produto_para_cadastrar)
    return

opcao = int(input('Cadastrar produto? 0 - Não     1 - Sim '))
while opcao == 1:
    produto_novo = {}
    
    produto_novo['codigo'] = int(input('Digite o código do produto: '))
    
    if produto_novo['codigo'] == 0:
        print('Código 0, encerrando cadastro de produtos.')
        break
    
    produto_novo['estoque'] = int(input('Digite a quantidade em estoque: '))
    produto_novo['minimo'] = int(input('Digite a quantidade mínima do estoque: '))
    
    cadastra_produto(produto_novo)
    opcao = int(input('Cadastrar produto? 0 - Não     1 - Sim '))

if len(lista) > 0:
    print('Lista de produtos por código em ordem crescente:')
    print("Código".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))

    for produto in sorted(lista, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))
else:
    print('Lista vazia.')

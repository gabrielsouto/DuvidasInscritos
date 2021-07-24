#veiculo = {'placa': "", 'montadora': "", 'modelo': "", 'ano': "", 'cor': ""}
estoque_de_carros = []

def cadastrar():
    #cadastrando veículo
    veiculo = {
        'Placa': "",
        'Montadora': "",
        'Modelo': "",
        'Ano': 0,
        'Cor': "" 
    }
    
    print("Digite os campos abaixo para cadastrar um veículo:")
    for indice in veiculo:
        veiculo[indice] = input(indice + ": ")
    
    estoque_de_carros.append(veiculo)
    
    print("Veículo cadastrado com sucesso.")
    
    return

def pesquisar():
    print('pesquisando carro')       
    return

def imprimir():
    #imprimindo lista de carros
    print('Estoque de carros')
    print("Nr".center(3), end='')
    print("Placa".center(14), end='')
    print("Montadora".center(18), end='')
    print("Modelo".center(12), end='')
    print("Ano".center(8))

    for posicao_e_veiculo in list(enumerate(estoque_de_carros, start=1)):
        
        posicao = posicao_e_veiculo[0]
        veiculo = posicao_e_veiculo[1]
        
        print(str(posicao).center(3), end='')
        print(str(veiculo['Placa']).center(14), end='')
        print(str(veiculo['Montadora']).center(18), end='')
        print(str(veiculo['Modelo']).center(12), end='')
        print(str(veiculo['Ano']).center(8))
        
    return

def remover():
    print('removendo carro') 
    return

def atualizar():
    print('atualizando carro') 
    return

def exibe_menu():
    print("Menu")
    print("1 - Cadastrar veículo")
    print("2 - Pesquisar veículo")
    print("3 - Imprimir veículos cadastrados")
    print("4 - Remover veículo")
    print("5 - Atualizar veículo")
    print("0 - Sair")

exibe_menu()
opcao = int(input())

while 0 <= opcao <= 5:
    
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        imprimir()    
    elif opcao == 4:
        remover()
    elif opcao == 5:
        atualizar()
    elif opcao == 0:
        print('Programa encerrado')
        exit()
    
    exibe_menu()
    opcao = int(input())
    
else:
    print('Opção inválida, programa encerrado')

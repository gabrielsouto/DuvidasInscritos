#veiculo = {'placa': "", 'montadora': "", 'modelo': "", 'ano': "", 'cor': ""}
estoque_de_carros = []
limite_estoque = 50

def cadastrar(indice_existente = None):
    #cadastrando veículo
    quantidade_carros_estoque = len(estoque_de_carros)
    
    if quantidade_carros_estoque < limite_estoque:
        veiculo = {
            'Placa': "",
            'Montadora': "",
            'Modelo': "",
            'Ano': 0,
            'Cor': "",
            'Proprietário': "" 
        }
        
        print("Digite os campos abaixo para cadastrar um veículo:")
        for indice in veiculo:
            veiculo[indice] = input(indice + ": ")
            
        if indice_existente is None:
            estoque_de_carros.append(veiculo)
            print("Veículo cadastrado com sucesso.")
        else:
            estoque_de_carros[indice_existente] = veiculo
            print("Veículo atualizado com sucesso.")
    else:
        print(f"Não é possível cadastrar mais carros. Limite de {limite_estoque} carros atingido.")
    
    return

def pesquisar():
    #pesquisando carro
    if len(estoque_de_carros) > 0:
        veiculo = {
                'Placa': "",
                'Montadora': "",
                'Modelo': "",
                'Ano': 0,
                'Cor': "",
                'Proprietário': "" 
            }
        
        carros_encontrados = []
        
        termo_pesquisa = input("Digite o termo a ser pesquisado no estoque de veículos: ")
        for indice in veiculo:
            carros_encontrados.extend([carro for carro in estoque_de_carros if termo_pesquisa.lower() in str(carro[indice]).lower()])
        
        if len(carros_encontrados) > 0:
            print('Estoque de carros')
            print("Nr".center(3), end='')
            print("Placa".center(14), end='')
            print("Montadora".center(18), end='')
            print("Modelo".center(12), end='')
            print("Ano".center(8), end='')
            print("Cor".center(12), end='')
            print("Proprietário".center(22))
            
            for posicao_e_veiculo in list(enumerate(carros_encontrados, start=1)):
                
                posicao_encontrada = posicao_e_veiculo[0]
                veiculo_encontrado = posicao_e_veiculo[1]
                
                print(str(posicao_encontrada).center(3), end='')
                print(str(veiculo_encontrado['Placa']).center(14), end='')
                print(str(veiculo_encontrado['Montadora']).center(18), end='')
                print(str(veiculo_encontrado['Modelo']).center(12), end='')
                print(str(veiculo_encontrado['Ano']).center(8), end='')
                print(str(veiculo_encontrado['Cor']).center(12), end='')
                print(str(veiculo_encontrado['Proprietário']).center(22))
        else:
            print(f"Nenhum veículo encontrado para o termo: {termo_pesquisa}")
    else:
        print("Não é possível pesquisar porque o estoque de carros está vazio.")
        
    return

def imprimir():
    #imprimindo lista de carros
    if len(estoque_de_carros) > 0:
        print('Estoque de carros')
        print("Nr".center(3), end='')
        print("Placa".center(14), end='')
        print("Montadora".center(18), end='')
        print("Modelo".center(12), end='')
        print("Ano".center(8), end='')
        print("Cor".center(12), end='')
        print("Proprietário".center(22))
        

        for posicao_e_veiculo in list(enumerate(estoque_de_carros, start=1)):
            
            posicao = posicao_e_veiculo[0]
            veiculo = posicao_e_veiculo[1]
            
            print(str(posicao).center(3), end='')
            print(str(veiculo['Placa']).center(14), end='')
            print(str(veiculo['Montadora']).center(18), end='')
            print(str(veiculo['Modelo']).center(12), end='')
            print(str(veiculo['Ano']).center(8), end='')
            print(str(veiculo['Cor']).center(12), end='')
            print(str(veiculo['Proprietário']).center(22))
    else:
        print("Estoque de carros vazio.")
    
    return

def imprimir_ordenado():
    #imprimindo lista de carros
    if len(estoque_de_carros) > 0:
        print('Estoque de carros')
        print("Nr".center(3), end='')
        print("Placa".center(14), end='')
        print("Montadora".center(18), end='')
        print("Modelo".center(12), end='')
        print("Ano".center(8), end='')
        print("Cor".center(12), end='')
        print("Proprietário".center(22))
        

        for posicao_e_veiculo in list(enumerate(sorted(estoque_de_carros, key=lambda item: item['Ano'], reverse=True), start=1)):
            
            posicao = posicao_e_veiculo[0]
            veiculo = posicao_e_veiculo[1]
            
            print(str(posicao).center(3), end='')
            print(str(veiculo['Placa']).center(14), end='')
            print(str(veiculo['Montadora']).center(18), end='')
            print(str(veiculo['Modelo']).center(12), end='')
            print(str(veiculo['Ano']).center(8), end='')
            print(str(veiculo['Cor']).center(12), end='')
            print(str(veiculo['Proprietário']).center(22))
    else:
        print("Estoque de carros vazio.")
    
    return

def remover():
    #removendo carro do estoque
    if len(estoque_de_carros) > 0:
        
        placa_informada = input("Digite a placa do veículo a ser removido do estoque de veículos: ")
        carros_encontrados_por_placa = [carro for carro in estoque_de_carros if placa_informada == str(carro['Placa'])]
        
        if len(carros_encontrados_por_placa) > 0:
            for carro_encontrado in carros_encontrados_por_placa:
                estoque_de_carros.remove(carro_encontrado)
            
            print(f"Foram removidos {len(carros_encontrados_por_placa)} veículos com a placa {placa_informada}")
        else:
            print(f"Não foram encontrados veículos com a placa {placa_informada}")
                            
    else:
        print("Não é possível remover nenhum veículo porque o estoque de carros está vazio.")
        
    return

def atualizar():
    #atualizar carro do estoque
    quantidade_carros_estoque = len(estoque_de_carros)
    
    if quantidade_carros_estoque > 0:
        
        imprimir()
        
        indice_informado = int(input("Digite o número do veículo a ser atualizado no estoque de veículos: "))
        
        if indice_informado > quantidade_carros_estoque or indice_informado < 1:
            print("O número do veículo precisa ser maior que zero e existir no estoque.")
        else:
            cadastrar(indice_informado-1)                            
    else:
        print("Não é possível atualizar nenhum veículo porque o estoque de carros está vazio.") 
    return

def exibe_menu():
    print(" ")
    print("Menu")
    print("1 - Cadastrar veículo")
    print("2 - Pesquisar veículo")
    print("3 - Imprimir veículos cadastrados")
    print("4 - Remover veículo")
    print("5 - Atualizar veículo")
    print("6 - Imprimir veículos por ano")
    print("0 - Sair")
    print(" ")
    
exibe_menu()
opcao = int(input())

while 0 <= opcao <= 6:
    
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
    elif opcao == 6:
        imprimir_ordenado()
    elif opcao == 0:
        print('Programa encerrado')
        exit()
    
    exibe_menu()
    opcao = int(input())
    
else:
    print('Opção inválida, programa encerrado')

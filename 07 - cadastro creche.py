opcao = None
lista_criancas = []

def matricular_crianca():
    crianca = {
      "Nome": "",
      "Data de Nascimento": "",
      "Idade": 0,
      "Responsável legal": "",
      "Peso": "",
      "Altura": "",
      "Turno": ""
    }
    
    print("Digite os campos abaixo para cadastrar uma criança:")
    for chave in crianca:
        crianca[chave] = input(chave + ":")
        
    lista_criancas.append(crianca)
    return
    
def listar_criancas():
    turno = input("Qual turno? Manhã, tarde ou integral?").lower()
    while turno not in ["manhã", "tarde", "integral"]:
        turno = input("Turno inválido. Manhã, tarde ou integral?").lower()
    
    for elemento in lista_criancas:
        if elemento["Turno"].lower() == turno:
            for chave in elemento:
                print(f"{chave}: {elemento[chave]}")
            print("-"*20)
    return
    
while opcao != "3":
    
    if opcao == "1":
        matricular_crianca()
    elif opcao == "2":
        listar_criancas()
    elif opcao == "3":
        break
    
    print("Digite o número da opção desejada:")
    print("1- Matricular criança")
    print("2- Lista das crianças matriculadas por turno")
    print("3- Sair")
    opcao = input()
    
    while opcao not in ["1", "2", "3"]:
        opcao = input("Opção inválida. 1, 2 ou 3?")

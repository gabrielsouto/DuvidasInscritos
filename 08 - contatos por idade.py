contatos = {}
contatos_maiores = {}
contatos_menores = {}

entrada = input("Deseja cadastrar um contato? (Aperte Enter para sair): ")

while entrada != "":
    nome = input("Nome: ")
    if nome == "":
        print("Nome vazio, encerrando programa.")
        break
    
    contatos[nome] = {"idade": 0, "telefone": ""}
    
    contatos[nome]["idade"] = int(input("Idade: "))
    contatos[nome]["telefone"] = input("Telefone: ")
    
    #pergunta se deseja continuar
    entrada = input("Deseja cadastrar um contato? (Aperte Enter para sair): ")
    
for nome in sorted(contatos):
    print(f"Nome: {nome} Idade: {contatos[nome]['idade']} Telefone: {contatos[nome]['telefone']}")
    
    if contatos[nome]['idade'] >= 18:
        contatos_maiores[nome] = {"idade": contatos[nome]['idade'], "telefone": contatos[nome]['telefone']}
    else:
        contatos_menores[nome] = {"idade": contatos[nome]['idade'], "telefone": contatos[nome]['telefone']}
        
    del contatos[nome]

if len(contatos_maiores) > 0:
    print("-" * 43)
    print("Contatos com idade maior ao igual a 18 anos")
    print("-" * 43)
    for nome in contatos_maiores:
        print(f"Nome: {nome} Idade: {contatos_maiores[nome]['idade']} Telefone: {contatos_maiores[nome]['telefone']}")

if len(contatos_menores) > 0:
    print("-" * 34)
    print("Contatos com idade menor a 18 anos")
    print("-" * 34)
    for nome in contatos_menores:
        print(f"Nome: {nome} Idade: {contatos_menores[nome]['idade']} Telefone: {contatos_menores[nome]['telefone']}")

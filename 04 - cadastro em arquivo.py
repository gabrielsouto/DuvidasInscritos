import os

cadastrar_aluno = 's'
nome_arquivo = "alunos.txt"
nome_escola = "ESCOLA MUNICIPAL FULANO DA SILVA"
separador = "-" * len(nome_escola)
cabecalho =  separador + "\n" + nome_escola + "\n" + separador

if not os.path.exists(nome_arquivo):
    arquivo_cadastro = open(nome_arquivo, 'w+t', encoding="utf-8")
    arquivo_cadastro.write(cabecalho)
    arquivo_cadastro.close()
    
def salvar_aluno(aluno):
    arquivo_cadastro = open(nome_arquivo, "r", encoding="utf-8")
    posicao_aluno = arquivo_cadastro.read().count("Aluno") + 1
    arquivo_cadastro.close()
    
    arquivo_cadastro = open(nome_arquivo, 'a+t', encoding="utf-8")
    arquivo_cadastro.write("\nAluno " + str(posicao_aluno) + "\n")
    
    for chave in aluno:
        arquivo_cadastro.write("- " + chave + ": " + aluno[chave] + "\n")
    
    arquivo_cadastro.write(separador)
    arquivo_cadastro.close()

while cadastrar_aluno == 's':
    #cadastro do aluno
    aluno = {
      "Nome": "",
      "CPF": "",
      "Mãe": "",
      "Data de Nascimento": "",
      "Idade": 0,
      "Série": ""
    }
    
    aluno["Nome"] = input("Digite o nome do aluno:")
    aluno["CPF"] = input("Digite o CPF do aluno:")
    aluno["Mãe"] = input("Digite o nome da mãe do aluno:")
    aluno["Data de Nascimento"] = input("Digite a data de nascimento do aluno:")
    aluno["Idade"] = input("Digite a idade do aluno:")
    aluno["Série"] = input("Digite a série do aluno:")
    
    '''    
    print("Digite os campos abaixo para cadastrar um aluno:")
    for chave in aluno:
        aluno[chave] = input(chave + ":")
    '''

    salvar_aluno(aluno)
    
    cadastrar_aluno = input("Deseja cadastrar mais um aluno? (s ou n)").lower()

#comando_abrir_arquivo = "notepad " + nome_arquivo
#os.system(comando_abrir_arquivo)

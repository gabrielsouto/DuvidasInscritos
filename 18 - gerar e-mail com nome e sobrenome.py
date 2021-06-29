def gera_email(nome:str, sobrenome:str):
    if len(nome) > 0 and len(sobrenome) > 0:
        return "Sr(a). " + nome + " " + sobrenome + ", seu e-mail é " + nome[0].lower() + sobrenome.lower() + "99@algoritmos.com.br"
    else:
        return None
            
print(gera_email('Gabriel', 'Souto'))
#como receber o nome e sobrenome do usuário:
#primeiro_nome = input('Digite o primeiro nome:')
#ultimo_sobrenome = input('Digite o último sobrenome:')
#print(gera_email(primeiro_nome, ultimo_sobrenome))

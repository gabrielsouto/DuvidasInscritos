import random

doadores = []

def cadastra_doador(nome:str, doacao:float):
    doadores.extend( ((nome + ' ') * int(doacao//10)).split() )
    return

def sorteia_ganhador():
    random.shuffle(doadores)
    print(f'Lista de doadores embaralhada: {doadores}')
    return random.choice(doadores)

opcao = int(input('Cadastrar doador? 0 - Não     1 - Sim '))

while opcao == 1:
    doador = input('Nome do doador: ')
    valor = float(input('Valor da doação: '))
    
    while len(doador.strip()) == 0 or valor < 10:
        print('O nome é obrigatório e o valor mínimo para doação é de R$ 10')
        doador = input('Nome do doador: ')
        valor = float(input('Valor da doação: '))
    
    cadastra_doador(doador, valor)
    
    opcao = int(input('Cadastrar doador? 0 - Não     1 - Sim '))

if len(doadores) > 0:
    print(f'Lista de doadores para sorteio: {doadores}')    
    print(f'O vencedor(a) foi: {sorteia_ganhador()}')

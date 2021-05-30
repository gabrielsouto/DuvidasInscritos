print("Digite o primeiro número inteiro para exibir as tabuadas no intervalo:")
a = int(input())

print("Digite o segundo número inteiro para exibir as tabuadas no intervalo:")
b = int(input())

if a > b:
    print('Nenhuma tabuada no intervalo!')
else:
    for multiplicador in range(a, b+1):
        for multiplicando in range(0, 11):
            print(f'{multiplicador} x {multiplicando} = {multiplicador*multiplicando}')
        print('-'*10)

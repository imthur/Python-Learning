numero = int(input('Digite um número inteiro: '))
while True:
    escolha = input('Digite "1" para antecessor, "2" para o sucessor ou "3" para encerrar o programa: ')
    if escolha != '1' and escolha != '2' and escolha != '3':
        print('Você digitou um caractere inválido! Tente novamente.')
    else:
        break
if escolha == '1':
    print(f'O antecessor de {numero} é: {numero - 1}.')
if escolha == '2':
    print(f'O sucessor de {numero} é: {numero + 1}.')
if escolha == '3':
    print('Programa finalizado.')
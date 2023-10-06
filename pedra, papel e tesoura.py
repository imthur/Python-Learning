nome1 = input('(Usuário 1) Digite seu nome: ')
nome2 = input('(Usuário 2) Digite seu nome: ')
loop = 's'
while loop == 's':
    print(f'[PEDRA PAPEL E TESOURA] \n DIGITE APENAS LETRAS MINÚSCULAS.')
    jogo = ['p', 'pp', 't']
    while True:
        p1 = input('Usuário 1, digite "p" para pedra, "pp" para papel ou "t" para tesoura: ')
        if p1 not in jogo:
            print('Você digitou um caractere inválido, tente novamente.')
        else:
            break
    while True:
        p2 = input('Usuário 2, digite "p" para pedra, "pp" para papel ou "t" para tesoura: ')
        if p1 not in jogo:
            print('Você digitou um caractere inválido, tente novamente.')
        else:
            break
    if p1 == p2:
        print('Empate!')
    elif p1 == 'pp' and p2 == 'p':
        print(f'{nome1} venceu!')
    elif p1 == 'p' and p2 == 't':
        print(f'{nome1} venceu!')
    elif p1 == 't' and p2 == 'pp':
        print(f'{nome1} venceu!')
    else:
        print(f'{nome2} venceu!')
    loop = input('Deseja jogar novamente? (s/n): ')

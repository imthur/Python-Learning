print('DIGITE APENAS LETRAS MINÚSCULAS.')
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
    print('Vitória do usuário 1!')
elif p1 == 'p' and p2 == 't':
    print('Vitória do usuário 1!')
elif p1 == 't' and p2 == 'pp':
    print('Vitória do usuário 1!')
else:
    print('Vitória do usuário 2!')
rep = 's'
while rep.lower() == 's':
    while True:
        num = float(input('Digite um número: '))
        if num == 0:
            print('Digite um número diferente de zero. ')
        else:
            break
    if num > 0:
        print('O número é positivo. ')
    else:
        print('O número é negativo.')
    rep = input('Deseja digitar outro número? (S/N): ')
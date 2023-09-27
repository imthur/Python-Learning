loop = 's'
while loop.lower() == 's':
    while True:
        base = float(input('Digite a base do triângulo: '))
        if base == 0:
            print('A base não pode ser 0. Tente novamente.')
        else:
            break
    while True:
        altura = float(input('Digite a altura do triângulo: '))
        if altura == 0:
            print('A altura não pode ser 0. Tente novamente.')
        else:
            break
    area = (base * altura)/2
    print(f'A área do triângulo é: {area}.')
    loop = input('Deseja repetir o programa? (S/N): ')
    if loop.lower() == 'n':
        print('Programa finalizado.')

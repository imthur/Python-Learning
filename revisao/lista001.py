rep = 's'
while rep.lower() == 's':
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) /2
    if media >= 7:
        print(f'Sua média foi: {media}, você foi aprovado!')
    elif media >= 4:
        print(f'Sua média foi: {media}, você está de recuperação.')
    else:
        print(f'Sua média foi: {media}, você foi reprovado. ')
    rep = input('Deseja calcular novamente? (S/N): ')

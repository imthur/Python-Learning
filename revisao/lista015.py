v1 = float(input(f'Digite o 1° valor: '))
while True:
    v2 = float(input(f'Digite o 2° valor: '))
    if v2 == v1:
        print('Os dois valores não podem ser iguais. Tente novamente.')
    else:
        break
if v1 > v2:
    print(v2, v1)
else:
    print(v1, v2)
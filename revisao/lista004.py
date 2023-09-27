n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2:
    if n1 > n3:
        print(f'O maior número é o primeiro: {n1}')
elif n2 > n1:
    if n2 > n3:
        print(f'O maior número é o segundo: {n2}')
else:
    print(f'O maior número é o terceiro: {n3}')

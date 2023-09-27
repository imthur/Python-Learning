a = []
impares = 0
pares = 0
positivos = 0
negativos = 0
zeros = 0
for x in range(10):
    a.append(int(input(f'Digite o {x+1}° valor: ')))
    if a[x] % 2 == 0:
        pares += 1
    if a[x] % 2 != 0:
        impares += 1
    if a[x] > 0:
        positivos += 1
    if a[x] < 0:
        negativos += 1
    if a[x] == 0:
        zeros += 1
print(f'Dentre os números digitados {pares} são pares, {impares} são ímpares, {positivos} são positivos, {negativos} são negativos e foram digitados {zeros} zeros.')
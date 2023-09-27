print('Digite -1 para finalizar as entradas.')
notas = []
loop = 's'
item = 0
acimaMedia = 0
while loop.lower() == 's':
    notas.append(float(input('Digite a nota: ')))
    if notas[item] == -1:
        loop = 'n'
    item += 1
notas.remove(-1)
print(f'A quantidade de notas lidas foi de: {item-1}.')
print(f'As notas foram: ')
for x in range(item-1):
    print(notas[x], end=' ')
print(f'\nAs notas ao contrário são: ')
for x in range(item, 1, -1):
    print(notas[x-2], end=' ')
print(f'\nA soma dos valores é: {sum(notas)}')
media = sum(notas)/(item-1)
print(f'A média das notas é: {media:.2f}')
for x in range(item-1):
    if notas[x] > media:
        acimaMedia += 1
print(f'O número de valores acima da média foi: {acimaMedia}.')
abaixoSete = 0
for x in range(item-1):
    if notas[x] < 7:
        abaixoSete += 1
print(f'O número de valores abaixo de 7 é: {abaixoSete}.')
print('PROGRAMA ENCERRADO.')
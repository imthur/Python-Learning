listaImpar = []
listaPar = []
listaNumeros = []
for x in range(20):
    listaNumeros.append(float(input(f'Digite o {x+1}° número: ')))
    if listaNumeros[x] % 2 == 0:
        listaPar.append(listaNumeros[x])
    else:
        listaImpar.append(listaNumeros[x])

print(f'Números digitados: {listaNumeros}.')
print(f'Números ímpares: {listaImpar}.')
print(f'Números pares: {listaPar}.')
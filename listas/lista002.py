lista = []
for x in range(10):
    lista.append(float(input(f'Digite o {x+1}° número: ')))
print('Os números digitados em ordem inversa são: ')
for x in range (9, -1, -1):
    print(lista[x], end = ' ')
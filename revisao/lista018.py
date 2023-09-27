lista = []
listaInversa = []
for x in range(5):
    lista.append(int(input('Digite 5 valores inteiros: ')))
for x in range(4, -1, -1):
    listaInversa.append(lista[x])
for x in range(5):
    print(listaInversa[x], end= ' ')
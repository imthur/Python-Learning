lista = []
numVogais = 0
numConsoante = 0
for x in range(10):
    lista.append(str(input('Digite uma letra: ')))
for x in range(10):
    letra = lista[x]
    if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
        numVogais += 1
    else:
        numConsoante += 1
print(f'Você digitou {numVogais} vogais e {numConsoante} consoantes.')

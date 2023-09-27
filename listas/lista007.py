listaNum = []
mul = 1
for x in range(5):
    listaNum.append(float(input(f'Digite o {x+1}° número: ')))
for x in range(5):
    mul += mul * listaNum[x]
print(sum(listaNum), mul, listaNum)
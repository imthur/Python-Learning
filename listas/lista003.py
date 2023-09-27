soma = 0
notas = []
count = 0
for x in range(4):
    notas.append(float(input(f'Digite a {x+1}° nota: ')))
for x in range(4):
    soma += notas[x]
    count += 1
media = soma/4
print(media)
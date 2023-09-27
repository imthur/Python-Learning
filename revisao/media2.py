'''l = int(input('Quantos números deseja digitar? '))
notas = []
for x in range(l):
    notas.append(float(input(f'Digite o {x+1}° número: ')))
soma = sum(notas)
media = sum(notas)/l
print(f'A soma das notas é: {soma}. \nA sua média foi de: {media}.')'''
l = int(input('Quantos números deseja digitar? '))
nota = 0
soma = 0
for x in range(l):
    nota = float(input(f'Digite a {x+1}° nota: '))
    soma += nota
    if soma > 1000:
        break
print(f'A soma dos números é: {soma}. A sua média foi de: {soma/l}.')
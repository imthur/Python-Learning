aprovados = 0
n1 = []
n2 = []
n3 = []
n4 = []
print('Primeiro aluno: ')
for x in range(4):
    n1.append(float(input(f'Digite a sua {x+1}° nota: ')))
media1 = sum(n1) / 4
print(f'Média primeiro aluno: {media1}.')
print('Segundo aluno: ')
for x in range(4):
    n2.append(float(input(f'Digite a sua {x+1}° nota: ')))
media2 = sum(n2) / 4
print(f'Média segundo aluno: {media2}.')
print('Terceiro aluno: ')
for x in range(4):
    n3.append(float(input(f'Digite a sua {x+1}° nota: ')))
media3 = sum(n3) / 4
print(f'Média terceiro aluno: {media3}.')
print('Quarto aluno: ')
for x in range(4):
    n4.append(float(input(f'Digite a sua {x+1}° nota: ')))
media4 = sum(n4) / 4
print(f'Média quarto aluno: {media4}.')
if media1 >= 7:
    aprovados += 1
if media2 >= 7:
    aprovados += 1
if media3 >= 7:
    aprovados += 1
if media4 >= 7:
    aprovados += 1
print(f'O número de alunos aprovados foi: {aprovados}.')
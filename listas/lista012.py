nomes = []
nomesPrint = []
idades = []
alturas = []
totalAlunos = 0
alturasPrint = []
for x in range(10):
    nomes.append((input(f'Digite o nome do {x+1}° aluno: ')))
for x in range(10):
    idades.append(int(input(f'Digite a idade do {x+1}° aluno: ')))
for x in range(10):
    alturas.append(float(input(f'Digite a altura do {x+1}° aluno: ')))
mediaAltura = int(sum(alturas)) / 10
for x in range(10):
    if idades[x] >= 13:
        if alturas[x] < mediaAltura:
            nomesPrint.append(nomes[x])
            alturasPrint.append(alturas[x])
            totalAlunos += 1
print(f'A média de altura da sala é: {mediaAltura}m. O número de alunos com 13 anos ou mais que tem a altura inferior à média é: {totalAlunos}. São eles: {nomesPrint}, com altura: {alturasPrint}m.')
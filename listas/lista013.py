meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
tempMedia = []
acimaMedia = []
mesesAcima = []
for x in range(12):
    tempMedia.append(float(input(f'Digite a temperatura média do mês de {meses[x]}: ')))
mediaAnual = int(sum(tempMedia)) / 12
for x in range(12):
    if tempMedia[x] > mediaAnual:
        acimaMedia.append(tempMedia[x])
        mesesAcima.append(meses[x])
print(f'A  média de temperatura anual é: {mediaAnual:.1f}°c. As temperaturas acima da média foram: {acimaMedia} e ocorreram nos meses de {mesesAcima}')
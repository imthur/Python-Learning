cidade = input('Digite o nome da cidade: ')
eleitores = int(input(f'Digite o número de Eleitores de {cidade}: '))
brancos = int(input(f'Digite a quantidade de votos brancos na eleição: '))
nulos = int(input(f'Digite a quantidade de votos nulos na eleição: '))
validos = int(input(f'Digite a quantidade de votos válidos na eleição: '))
porcentagemB = (brancos/eleitores) * 100
porcentagemN = (nulos/eleitores) * 100
porcentagemV = (validos/eleitores) * 100
print(f'Os votos brancos representam {porcentagemB:.2f}% do total de eleitores, os nulos {porcentagemN:.2f}% e os válidos {porcentagemV:.2f}% na cidade de {cidade}.')
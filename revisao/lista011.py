idadeAnos = int(input('Digite sua idade(anos): '))
idadeMeses = int(input('Digite sua idade(meses): '))
totalDias = (idadeAnos * 365) + (idadeMeses * 30) + int(input('Digite sua idade(dias): '))
print(f'No total você viveu: {totalDias} dias.')
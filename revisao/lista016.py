print('Formato 24h.')
inicio = int(input('Digite a hora de início do jogo: '))
fim = int(input('Digite a hora de fim do jogo: '))
if inicio < 12:
    inicio += 12
if fim < 12:
    fim += 12
total = inicio - fim
if total < 0:
    total += 24
print(f'A duração do jogo foi de: {total}h.')
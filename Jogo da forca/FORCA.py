import random
import time
from biblioteca import frutas, objetos, paises, profissoes, esportes, boneco
loop = True
import os
ganhou = 'n'
vitorias = 0
derrotas = 0
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def palavraOculta(palavra, acertos):
    resultado = ''
    for letra in palavra:
        if letra in acertos:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado
print('JOGO DA FORCA'.center(19, '='))
print('Seja bem-vindo!'.center(19))
usuario = input('Digite seu nome: ').title()
clear()
while loop:
    chances = 6
    acertos = []
    erros = []
    print('JOGO DA FORCA'.center(19, '='))
    todasAsPalavras = frutas + objetos + paises + profissoes + esportes
    palavra = random.choice(todasAsPalavras)
    if palavra in frutas:
        dica = 'Dica: é uma fruta.'
    if palavra in objetos:
        dica = 'Dica: é um objeto.'
    if palavra in paises:
        dica = 'Dica: é um país.'
    if palavra in profissoes:
        dica = 'Dica: é uma profissão.'
    if palavra in esportes:
        dica = 'Dica: é um esporte.'
    while chances > 0:
        print(boneco(chances))
        print(dica)
        print()
        print(f'{palavraOculta(palavra, acertos)}'.center(19))
        print()
        print(f'Letras erradas: {", ".join(erros)}')
        while True:
            tentativa = input('• Digite uma letra: ').upper()
            clear()
            c = 0
            for x in tentativa:
                if x not in alfabeto:
                    c += 2
                c += 1
            if c > 1:
                print('Você digitou mais de uma letra ou um caractere inválido. Tente novamente!')
            elif tentativa in acertos or tentativa in erros:
                print(f'A letra {tentativa} já foi digitada, tente novamente!')
            else:
                break
        if tentativa in palavra:
            acertos.append(tentativa)
            if all(letra in acertos for letra in palavra):
                clear()
                print(f'Parabéns, você ganhou! A palavra era: {palavra}.')
                vitorias += 1
                break
        else:
            erros.append(tentativa)
            chances -= 1
            print(f'Letra incorreta.')
            time.sleep(0.4)
            clear()
    if chances == 0:
        print(f'Você perdeu! A palavra era: {palavra}.')
        derrotas += 1
    print('PONTUAÇÃO'.center(30, '='))
    print(f'Usuário: {usuario}')
    print(f'\nVitórias: {vitorias}\nDerrotas: {derrotas}')
    questao = input('Deseja jogar novamente? (s/n): ')
    if questao.lower() == 'n':
        loop = False
    else:
        clear()
print('Programa finalizado! Obrigado por jogar.')

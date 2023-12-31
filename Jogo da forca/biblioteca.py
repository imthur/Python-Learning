import os
frutas = ['MORANGO', 'ABACAXI', 'MAMAO', 'PERA', 'UVA', 'MANGA', 'LARANJA', 'MACA', 'BANANA', 'KIWI', 'ABACATE', 'ABACAXI', 'AMEIXA', 'MELANCIA', 'PESSEGO', 'LIMAO', 'FIGO', 'COCO']
objetos = ['FACA', 'TESOURA', 'LAPIS', 'PORTA', 'CADEIRA', 'MESA', 'CANETA', 'CADERNO', 'CELULAR', 'TELEVISAO', 'CARRO', 'BICICLETA', 'ANEL', 'OCULOS', 'RELOGIO', 'CHAVE', 'MARTELO', 'COLHER', 'GARRAFA', 'XICARA']
paises = ['BRASIL', 'VENEZUELA', 'ESPANHA', 'INGLATERRA', 'COLOMBIA', 'CUBA', 'CHINA', 'INDIA', 'INDONESIA', 'PAQUISTAO', 'NIGERIA', 'RUSSIA', 'MEXICO', 'JAPAO', 'ETIOPIA', 'EGITO', 'VIETNA', 'TAILANDIA', 'ARGENTINA', 'PERU']
profissoes = ['MEDICO', 'ENGENHEIRO', 'ADVOGADO', 'PROFESSOR', 'MUSICO', 'ARTISTA', 'ATLETA', 'COZINHEIRO', 'BOMBEIRO', 'POLICIAL', 'ELETRICISTA', 'FOTOGRAFO', 'CIENTISTA', 'PSICOLOGO', 'JORNALISTA', 'ARQUITETO', 'FARMACEUTICO', 'PILOTO', 'VETERINARIO', 'DENTISTA']
esportes = ['FUTEBOL', 'BASQUETE', 'TENIS', 'NATACAO', 'VOLEI', 'GINASTICA', 'ATLETISMO', 'HANDEBOL', 'CICLISMO', 'SURF', 'ESCALADA', 'SKATE', 'GOLFE', 'JUDO', 'BOXE', 'FUTSAL', 'MMA', 'BEISEBOL', 'RUGBY']
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def palavraOculta(palavra, acertos):
    resultado = ''
    for letra in palavra:
        if letra in acertos:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def boneco(chances):
    if chances == 6:
        return f'_____\n|\n|\n|'
    if chances == 5:
        return f'_____\n|  O\n| \n|'
    if chances == 4:
        return f'_____\n|  O\n|  |\n|'
    if chances == 3:
        return f'_____\n|  O\n| /|\n|'
    if chances == 2:
        return f'_____\n|  O\n| /|\ \n|'
    if chances == 1:
        return f'_____\n|  O\n| /|\ \n| / '
    if chances == 0:
        return f'_____\n|  O\n| /|\ \n| /\ '

def score(usuario, vitorias, derrotas):
    tam = 30

    pontuacao = {
        "Usuário": usuario,
        "Acertos": vitorias,
        "Erros": derrotas,
    }
    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"PONTUAÇÃO":^{tam}}|')
        print(f'+{"-" * tam}+')
        for k, v in pontuacao.items():
            print(f'|{f" {k} - {v}":{tam}}|')
        print(f"+{'-' * tam}+")
        break

def cabecI():
    tam = 30

    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"JOGO DA FORCA":^{tam}}|')
        print(f'+{"-" * tam}+')
        print(f'|{f"Seja bem vindo(a)":{tam}}|')
        print(f"+{'-' * tam}+")
        break

def cabec():
    tam = 30

    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"JOGO DA FORCA":^{tam}}|')
        print(f'+{"-" * tam}+')
        break

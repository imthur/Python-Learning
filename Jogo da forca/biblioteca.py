frutas = ['MORANGO', 'ABACAXI', 'MAMAO', 'PERA', 'UVA', 'MANGA', 'LARANJA', 'MACA', 'BANANA', 'KIWI', 'ABACATE', 'ABACAXI', 'AMEIXA', 'MELANCIA', 'PESSEGO', 'NECTARINA', 'LIMAO', 'LIMA', 'FIGO', 'COCO']
objetos = ['FACA', 'TESOURA', 'LAPIS', 'PORTA', 'CADEIRA', 'MESA', 'CANETA', 'CADERNO', 'CELULAR', 'TELEVISAO', 'CARRO', 'BICICLETA', 'ANEL', 'OCULOS', 'RELOGIO', 'CHAVE', 'MARTELO', 'COLHER', 'GARRAFA', 'XICARA']
paises = ['BRASIL', 'VENEZUELA', 'ESPANHA', 'INGLATERRA', 'COLOMBIA', 'CUBA', 'CHINA', 'INDIA', 'INDONESIA', 'PAQUISTAO', 'NIGERIA', 'RUSSIA', 'MEXICO', 'JAPAO', 'ETIOPIA', 'EGITO', 'VIETNA', 'TAILANDIA', 'ARGENTINA', 'PERU']
profissoes = ['MEDICO', 'ENGENHEIRO', 'ADVOGADO', 'PROFESSOR', 'MUSICO', 'ARTISTA', 'ATLETA', 'COZINHEIRO', 'BOMBEIRO', 'POLICIAL', 'ELETRICISTA', 'FOTOGRAFO', 'CIENTISTA', 'PSICOLOGO', 'JORNALISTA', 'ARQUITETO', 'PILOTO', 'VETERINARIO', 'DENTISTA']
esportes = ['FUTEBOL', 'BASQUETE', 'TENIS', 'NATACAO', 'VOLEI', 'GINASTICA', 'ATLETISMO', 'HANDEBOL', 'CICLISMO', 'SURF', 'ESCALADA', 'SKATE', 'GOLFE', 'JUDO', 'BOXE', 'FUTSAL', 'MMA', 'BEISEBOL', 'RUGBY']
def boneco(chances):
    if chances == 6:
        return f'_____\n|\n|\n|'
    if chances == 5:
        return f'_____\n|  O\n| \n|'
    if chances == 4:
        return f'_____\n|  O\n|   |\n|'
    if chances == 3:
        return f'_____\n|  O\n| /|\n|'
    if chances == 2:
        return f'___\n   O \n| /|\ \n'
    if chances == 1:
        return f'_____\n|  O\n| /|\ \n| / '
    if chances == 0:
        return f'_____\n|  O\n| /|\ \n| /\ '

from bibliotecaTamagochi import Tamagochi
nome = input('Digite o nome do seu tamagochi: ').title()
idade = float(input(f'Digite a idade de {nome}: '))
peso = float(input(f'Digite o peso de {nome}: '))
t1 = Tamagochi(nome, idade, peso)
print('1. Comer .......... 2. Falar\n3. Dormir ......... 4. Parar de Comer\n5. Parar de Falar . 6. Acordar\n0. Sair')
loop = True
while loop:
    c = int(input(f'O que deseja que {nome} faça agora? '))
    if c == 1:
        t1.comer()
    if c == 2:
        t1.falar()
    if c == 3:
        t1.dormir()
    if c == 4:
        t1.pararComer()
    if c == 5:
        t1.pararFalar()
    if c == 6:
        t1.pararDormir()
    if c == 0:
        loop = False
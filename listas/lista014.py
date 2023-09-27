perguntas = []
envolvimento = 0
print('TESTE DE ENVOLVIMENTO NO CRIME')
perguntas.append(input(f'Telefonou para a vítima? (S/N): '))
perguntas.append(input(f'Esteve no local do crime? (S/N): '))
perguntas.append(input(f'Mora perto da vítima? (S/N): '))
perguntas.append(input(f'Devia para a vítima? (S/N): '))
perguntas.append(input(f'Já trabalhou com a vítima? (S/N): '))
for x in range(5):
    if perguntas[x].lower() == 's':
        envolvimento += 1
print('==========================================')
if envolvimento < 2:
    print('A pessoa foi classificada como INOCENTE.')
if envolvimento == 2:
    print('A pessoa foi classificada como SUSPEITA.')
if envolvimento == 3 or envolvimento == 4:
    print('A pessoa foi classificada como CÚMPLICE.')
if envolvimento == 5:
    print('A pessoa foi classificada como CULPADA.')
print('==========================================')
salario = 200
vendasBrutas = []
vendedores = []
comissao = []
salarioTotal = []
#Rank um: Recebe entre $200 e $500.
rankUm = 0
nomesR1 = []
#Rank dois: Recebe entre $500 e $800.
rankDois = 0
nomesR2 = []
#Rank três: Recebe acima de $800.
rankTres = 0
nomesR3 = []
qtdV = int(input('Digite o número de vendedores que você emprega: '))
for x in range(qtdV):
    vendedores.append(input(f'Digite o nome do  {x+1}° vendedor: '))
for x in range(qtdV):
    vendasBrutas.append(float(input(f'Digite o valor bruto das vendas de {vendedores[x]}: ')))
for x in range(qtdV):
    comissao.append(vendasBrutas[x]*0.09)
    salarioTotal.append(salario + comissao[x])
for x in range(qtdV):
    if salarioTotal[x] > 200 and salarioTotal[x] < 500:
        rankUm += 1
        nomesR1.append(vendedores[x])
    if salarioTotal[x] >= 500 and salarioTotal[x] < 800:
        rankDois += 1
        nomesR2.append(vendedores[x])
    if salarioTotal[x] >= 800:
        rankTres += 1
        nomesR3.append(vendedores[x])
print(f'O número de vendedores que recebem entre $200 e $500 é: {rankUm}.')
print('São eles:')
for x in nomesR1:
    print(x, end=" ")
print(f'O número de vendedores que recebem entre $500 e $800 é: {rankDois}.')
print('São eles:')
for x in nomesR2:
    print(x, end=" ")
print(f'O número de vendedores que recebem acima de $800 é: {rankTres}.')
print('São eles:')
for x in nomesR3:
    print(x, end=" ")
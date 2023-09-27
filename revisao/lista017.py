qtd = int(input('Digite o número de maçãs compradas: '))
if qtd > 12:
    total = qtd * 1
else:
    total = qtd * 1.3
print(f'O valor total do pedido foi de: R$ {total:.2f}.')
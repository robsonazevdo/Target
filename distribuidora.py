

#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

estado = ['SP', 'RJ', 'MG', 'ES', 'OUTROS']
valor = [67.83643, 36.67866, 29.22988, 27.16548, 19.84953]
total = 0
cont = 0

for i in range(0, len(valor)):
    total += valor[i]


for v in valor:
    cont += 1
    percentual = ((v / total) * 100)
    print(f'O percentual de faturamento de {estado[cont - 1]} é: {percentual:.2f}%')


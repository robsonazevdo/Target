import json

''' Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.'''


with open('dados.json', 'r') as Dados_json:
    dados = json.load(Dados_json)





def menor():
    menor = 100000.0000
   
    for i in range(0, len(dados)):

        if dados[i]['valor'] != 0:
            if dados[i]['valor'] < menor:
                menor = dados[i]['valor']

    return menor



def maior():
    maior = 0

    for i in range(0, len(dados)):
        if dados[i]['valor'] > maior:
            maior = dados[i]['valor']
        
    return maior



def media():
    soma = 0
    cont = 0
    dias = 0
    for i in range(0, len(dados)):

        if dados[i]['valor'] != 0:
            soma += dados[i]['valor']
            cont += 1

    media = soma / cont

    for k in range(0, len(dados)):

        if dados[k]['valor'] != 0 and dados[k]['valor'] > media:
            dias += 1


    return dias    



print(f"O menor valor de faturamento ocorrido em um dia do mês: {menor()} ")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {maior()}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {media()}")




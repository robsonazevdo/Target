
# Escreva um programa que inverta os caracteres de um string.

frase = 'Invertendo_caracteres'
c = list(frase)

cont = len(c)
lista = []

for i in range(cont,0,-1):
    lista.append(c[i-1])

print(''.join(lista))

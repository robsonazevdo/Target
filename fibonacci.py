from random import randint

#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 
# valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem 
# que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem
#  avisando se o número informado pertence ou não a sequência.

n = randint(0,50)
ultimo=0
penultimo=1

lista = []
count=0
while count <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    lista.append(ultimo)
    count += 1

if n in lista:
    print('O número %d Pertence a sequência' %(n))
else:
    print('O número %d Não Pertence a sequência' %(n))



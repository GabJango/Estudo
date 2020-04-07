# Exercício Python 016: Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção Inteira.
from math import floor
from math import trunc
num = float(input('Digite um valor:'))
print('O número intero do valor {} é {}'.format(num, floor(num)))
print('O número digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
print('O número digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

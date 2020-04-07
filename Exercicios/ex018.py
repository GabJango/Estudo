# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import radians, cos, sin, tan
num = int(input('Digite o Valor de um Angulo:'))
radian = radians(num)
print('Dado o angulo {}'.format(num))
print('Temos seu coseno sendo {:.2f}'.format(cos(radian)))
print('Temos seu Seno sendo {:.2f}'.format(sin(radian)))
print('Temos sua Tangente sendo {:.2f}'.format(tan(radian)))

#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

from math import hypot
catop = float(input('Informe o valor do cateto oposto:'))
catadj = float(input('Infor o valor do cateto adjacente ao angulo:'))
hypotenu = hypot(catop, catadj)
hip = (catop ** 2 * catadj ** 2) ** (1/2)
print('A hipotenusa entre o cateto oposto de valor {} e cateto adjacente de valor {} é igual a {:.2f}'.format(catop, catadj, hypotenu))

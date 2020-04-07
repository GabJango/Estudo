import json  # Comando generalista
from json import encoder # Comandos especifico
#biblioteca math
import math  #Importando todas as funcionalidades
# quando importamos a bliblioteca math percebemos que ao usar (.) após a função ela nos traz mais resultados
from math import sqrt, floor  # Dessa forma podemos usar apelas floor()
# from math import sqrt
# elas são,
# ceil - Arredondar para cima
# floor - Arredondar para baixo
# trunc - Truncar o valor, ou seja, cortar valor da virgula para a direita
# pow - Poténcia de um valor
# sqrt - Raiz quadrada do valor
# factorial - fatorial do valor

import random # bibliteca para gerar numeros aleatorio
import emoji

num = input('Digite um valor: ')
raiz = math.sqrt(num)
print('A raiz do valor {} é igual a {:.2f}'.format(num, math.ceil(raiz)))
print('A raiz do valor {} é igual a {:.2f}'.format(num, floor(raiz)))
num1 = random.random()  # para um número de 0 a 1
num2 = random.randint(1, 10)  # para um numero inteiro
print('O valor randomico é : {}'.format(num1))
print('O valor randomico inteiro é : {}'.format(num2))
print(emoji.emojize('Olá mundo, :earth_americas:', use_aliases=True))

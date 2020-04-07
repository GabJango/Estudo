# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle, sample
from itertools import count
aluno1 = input('Digite o nome do Primeiro aluno:')
aluno2 = input('Digite o nome do Segundo aluno:')
aluno3 = input('Digite o nome do Terceiro Aluno:')
aluno4 = input('Digite o nome do Quarto Aluno:')
alunos = [aluno1, aluno2, aluno3, aluno4]
seq = sample(alunos, 4)
print('A sequência de apresentação dos trabalhos é')
print(*(map('{}: {}'.format, count(), seq)), sep="\n")
seq2 = shuffle(alunos)
print('A sequencia de apresentação dos trabalhos sera:')
print(alunos)

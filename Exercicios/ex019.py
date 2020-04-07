# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
aluno1 = str(input('Digito nome do primeiro aluno:'))
aluno2 = str(input('Digito nome do segundo aluno:'))
aluno3 = str(input('Digito nome do terceiro aluno:'))
aluno4 = str(input('Digito nome do quarto aluno:'))
alunos = [aluno1, aluno2, aluno3, aluno4]  # Lista em python tem que estar entre colchetes
alunos2 = aluno1, aluno2, aluno3, aluno4  # Tupla quando sonegamos []
escolhido = choice(alunos)
print('O aluno escolhido para apagar a lousa foi {} !'.format(escolhido))
print(alunos, type(alunos))
print(alunos2, type(alunos2))

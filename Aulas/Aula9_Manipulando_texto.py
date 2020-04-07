# Para o python toda string está entre aspas ('' ou "")
# A string é salva na memória
# Python diferencia maisucula e minuscula
frase = 'Curso em Video Python'
#  C|U|R|S|O| |E|M| |V|I |D |E |O |  |P |Y |T |H |O |N|
# 0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|

# Fatiamento ( OPERAÇÕES )
print(frase)
print(frase[9])  # Printa a letra do indice 9 ou seja 'V'
print(frase[9:13])  # Printa do indice 9 até a letra 13 (Lembrado 13 ele desconsidera) = 'Vide'
print(frase[9:21:2])  # Começa no 9 para no 21 pulando de dois em dois
print(frase[:5])  # Começa no incio e vai até o 5
print(frase[9:])   # Printa do indice 9 até o fim
print(frase[9::3])  # Começa do 9 e vai até o fim pulando de 3 em 3

# análise de string ( FUNCIONALIDADES )
print(len(frase))  # Comprimento da frase 21
print(frase.count('o'))  # Conta quantas vezes aparece a letra 'o' lembrando do case sensitive
print(frase.count('o', 0, 13))  # Faz uma contagem com fatiamento, do 0 até 13 onde tem 'o'
print(frase.find('deo'))  # Quantas vezes ele encontrou 'deo', ele vai mostrar onde começou a posição
print(frase.find('Android'))  # Quando não existe ele retorna posição -1
print('Curso' in frase)  # Dentro da frase existe a palavra 'Curso' (Isso é um operador nao funcionalidade)

#Tranformação
# uma lista de string é imutavel nao conseguimos mexer nela
print(frase.replace('Python','Android'))  #Replace ele procura a string "Pyhton" e Substitui por Android"+
print(frase.upper())  # Deixa a frase toda em maiusculas (Upper é um metodo)
print(frase.lower())  # Deixa toda a frase em minusculo
print(frase.capitalize())  # Capitalize joga todos os caracteres para minusculo e somente o primeiro caracter maiusculo
print(frase.title())  # Title é mais profundo ele analisa toda a frase e deixa maisculo cada inicio de palavra

frase2 = "   Aprenda Python  "
# / / / /A/P/R/E/N/D/A/  /P /Y /T /H /O /N /  /  /
#/0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/

print(frase2.strip())  # Ele remove todos os espaços inuteis no início e no final da string
print(frase2.rstrip())  # igual strip porém somente o lado direto da string sera removido (espaços)
print(frase2.lstrip())  # de forma analoga temos lstrip que remove espaços da string do lado esquerdo

#Divisão
print(frase.split())  # Por padrão o split é feito entre os espaços, onde está os espaços ele coloca uma divisão
# Então basicamente ele gera uma lista a partir de uma frase com espaços.
#  |C|U|R|S|O| |E|M| |V|I|D|E|O| |P|Y|T|H|O|N|
# |0|1|2|3|4| |0|1| |0|1|2|3|4| |0|1|2|3|4|5|

#junção
print('-'.join(frase)) # por exemplo, serve para juntar famílias de micro-memórias com o que esta entre as aspas
# Curso-Em-Video-Python
# C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n
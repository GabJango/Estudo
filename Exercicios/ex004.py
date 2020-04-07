x = input('Digite algo:')
print('O tipo primitivo é', type(x))
# Verifica o tipo que é a variavel

print('É possível inverter para valor do tipo INT (é numérico)?', x.isnumeric())
# É possível inverter para valor do tipo INT?

print('É número alpha?', x.isalpha())
# É número alpha? (alphabético)

print('É alpha numérico?', x.isalnum())
# É alpha numérico"

print('É maiusculo?', x.isupper())
# É maiusculo?"

print('É Decimal?', x.isdecimal())
# Valor Decimal?

print('É valor ASCII?', x.isascii())
# Valor ta tabela ASCII

print('É digit?', x.isdigit())
# verifica se a string consiste apenas em dígitos.

print('É identificador?', x.isidentifier())
# se todos os caracteres são válidos para escrever um
# identificador no código, então eles são letras maiúsculas e
# minúsculas, dígitos, desde que não seja o primeiro caractere e mais
# alguns caracteres Unicode

print('É minusculo?', x.islower())
# Verifica se todos os caracteres são minusculos

print('pode ser printado?', x.isprintable())
# é uma string pré-inicializada usada como constante de string.
# No Python, string.printable fornecerá todos os conjuntos de pontuação,
# dígitos, boletins ascii e espaço em branco.

print('É espaços?', x.isspace())
# retorna True se houver apenas caracteres de espaço em branco na string.
# Caso contrário, ele retornará False

print('Esta capitalizada (título) ?', x.istitle())
# verifica se todos os caracteres baseados em maiúsculas e
# minúsculas na sequência que segue as letras sem maiúsculas
# e minúsculas estão em maiúsculas e todos os outros caracteres
# baseados em maiúsculas e minúsculas.
# Ou seja começa maiúscula

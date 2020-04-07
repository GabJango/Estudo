# Aula sobre operadores aritiméticas ou seja (+, -, *, /, **, //, %)
#  + = Adição
#  - = Subtração
#  * = multiplicação
#  ** = potênciação ou pow(x,elevado a y)
#  // = divisão inteira
#  % = resto da divisão
# == simbolo de igualdade

5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
pow(5, 2) == 25
5 // 2 == 2
5 % 2 == 1

# Ordem de precedências dos operadores aritiméticos
# 1 = ()
# 2 = **
# 3 = *, /, //, %
# 4 = +, -

# Exemplos

5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243

# Parte A

nome = str(input('Qual é seu nome? '))
print('Prazer em te conhecer {:>20}! '.format(nome))  # Alinhamento a direita
print('Prazer em te conhecer {:<20}! '.format(nome))  # Alinhamento a esquerda
print('Prazer em te conhecer {:^20}! '.format(nome))  # Centralizado em 20 espaços
print('Prazer em te conhecer {:=^20}! '.format(nome))  # Centralizado em 20 espaços trocando espaços por '='

# Parte A²
n1 = int(input('Digite uma valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n a multiplicação vale {}, \n a Divisão vale {:.2f}'.format(s, m, d))
# DIVISÃO VALE, 2 casa depois da vírgula {:.2f}
# \n quebrar linha

print('A soma vale {}, a multiplicação vale {}, a Divisão vale {:.3f}'.format(s, m, d), end=' ')
# DIVISÃO VALE, 3 casa depois da vírgula
# para não quebrarmos a linhas usamos no fina (, end=' ')

print('A divisão inteira vale {}, a exponeciação vale {}'.format(di, e))

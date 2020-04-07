# Alguns tipos primitivos sao
# int = 0, -4, 1, 5, 9898
# float = 0.2, 1,4, -5,55, 7.0 (numeros reais)
# bool = True, False (Lembrando primeira letra maiuscula)
# str = '2
# 1', 'ola' (contem '' )

n1 = int(input("Digite um valor: "))  # Colocando um tipo primitivo na variavel, no caso int(), inteiro
n2 = int(input("Digite outro valor: "))
print(type(n1))  # Mostra o tipo da variavel
print(type(n2))
n3 = n1 + n2
print('A soma entre', n1, 'e', n2, 'vale', n3)
print("A soma entre {} e {} vale {}".format(n1, n2, n3))  # Forma mais enxuta

n4 = float(input('Digite um valor: '))
print(n4)
n5 = bool(input('Digite uma valor: '))
print(n5)
n6 = input('Digite valor verificação: ')
# print(n5.isnumeric()) não é possível fazer isso com valores booleanos
# print(n4.isnumeric()) não é possível fazer isso com valores float
# print (n1.isnumeric()) (n2.isnumeric()) não é possível pois é int

print('É possível inverter para valor do tipo INT (é numérico)?', n6.isnumeric())
# É possível inverter para valor do tipo INT?

print("É número alpha?", n6.isalpha())
# É número alpha? (alphabético)

print("É alpha numérico?", n6.isalnum())
# É alpha numérico"

print("É maiusculo?", n6.isupper())
# É maiusculo?"

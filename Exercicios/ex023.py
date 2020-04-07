num = int(input('Digite um valor de 0 a 9999:'))
print('O valor digitado é {}'.format(num))
unidade = num % 10
dezena = int(((num - unidade) / 10) % 10)
centena = int((((((num - unidade)/ 10))- dezena) / 10) % 10)
milhar = int(((((((((num - unidade)/  10))- dezena) / 10 ) - centena)) / 10) % 10)

print('O valor da unidade é {}'.format(unidade))
print('O valor da dezena é {}'.format(dezena))
print('O valor da centena é {}'.format(centena))
print('O valor do milhar é {}'.format(milhar))
#Formato quando tipo string
#print('O valor da sua unidade é {}'.format(num[0]))
#print('O valor da sua dezena é {}'.format(num[1]))
#print('O valor da sua centena é {}'.format(num[2]))
#print('O valor do seu milhar é {}'.format(num[3]))

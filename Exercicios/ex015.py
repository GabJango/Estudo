dias = int(input('Por quandos dias o carro ficou alugado?'))
km = float(input('Quantos Km foram rodados no total?'))
pagardia = dias * 60.00
kmtotal = km * 0.15
totalpagar = pagardia + kmtotal
totalpagar2 = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(totalpagar))
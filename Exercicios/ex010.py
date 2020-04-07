import requests
n1 = float(input('Quanto dinheiro você tem na carteira?RS'))
url = "https://economia.awesomeapi.com.br/all/USD-BRL"
response = requests.get(url)
data = response.json()
dolar = float(data['USD']['high'])
total = n1 / dolar
print('Você tem R${:.2f} Reais, você pode comprar US{:.2f} Dolares '.format(n1, total))

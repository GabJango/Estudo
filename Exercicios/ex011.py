l1 = float(input('Digite a altura da parede:'))
l2 = float(input('Digite a Largura da parede:'))
area = l1 * l2
balde = area / 2
print('Com sua parede contendo {} de altura e {} de largura,'.format(l1, l2), end='')
print('voce precisa de {} baldes de tinta para pintar toda a parede.'.format(balde))

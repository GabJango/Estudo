# ----------------------------------------------------------------------
# Created by: Gabriel de Nadai
# ----------------------------------------------------------------------
# Esta função altera o nome do arquivo antigo, alterando nome imagem para screenshot
# Em seguida ele altera o datetime para timestamp.
# ----------------------------------------------------------------------
import os
from datetime import datetime

# Local que contém os arquivos a serem alterados.
filename = 'C:/Users/Nadai/Pictures/Screenshot/'
for oldname in os.listdir(filename):
    # So altera os arquivo que iniciam com 'imagem'
    if oldname[0:6] == 'imagem':
        data = int(oldname[6:16])  # pega o datetime
        timestamp = str(datetime.fromtimestamp(data))  # transforma date time em timestamp
        newname = oldname[0:6] + timestamp  # monta imagem + timestamp
        newname = newname.replace(' ', '_')  # troca ' ' por '_'
        newname = newname.replace(':', '-')  # troca ':' por '-'
        newname = newname.replace('imagem', 'screenshot')  # altera a imagem no inicio para screenshot
        newname = newname + '.png'  # adiciona a extensao no arquivo
        print(newname)  # Mostra os novos nomes
        # Renomeia todos arquivos
        os.rename(os.path.join(filename, oldname),
                  os.path.join(filename, newname))


print("Renomeado")

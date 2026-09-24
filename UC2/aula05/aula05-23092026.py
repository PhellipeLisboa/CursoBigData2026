import pandas as pd
import numpy as np

import matplotlib.pyplot as plt  
import seaborn as sns  

# lista_numeros = [10, 20, 30, 40, 50]
# meu_array = np.array(lista_numeros)

# minha_serie = pd.Series(lista_numeros)

# Comparando com uma série do Pandas
# minha_serie = pd.Series(lista_numeros)
# print(minha_serie)
# print(type(minha_serie))


precos_array = np.genfromtxt('C:\\Users\\phellipe.barbosa\\Documents\\BIGDATA\\CursoBigData2026\\UC2\\aula03\\vendas_produtos.csv', delimiter=',', skip_header=1, dtype=None, encoding='utf-8', usecols=3)
print(precos_array)
print(type(precos_array))

media = np.mean(precos_array)
print(f"Média dos preços: R$ {media:.2f}")

mediana = np.median(precos_array)
print(f"Mediana dos precos: R$ {mediana:.2f}")

# Calcule a distância entre a média e a mediana:
distancia = (media - mediana) / mediana
print(f"Distância entre a média e a mediana: {distancia * 100:.2f}%")

if abs(distancia) <= 0.10:
    print("A média tende a ser uma medida de tendência central confiável.")
elif abs(distancia) < 0.25:
    print("A média pode estar sofrendo uma influência moderada de valores extremos.")
else:
    print("A média tende a não ser uma medida de tendência central confiável.")

# Verificando a direção da influência
if media > mediana:
    print("A influência é dos valores mais altos da distribuição.")
elif media < mediana:
    print("A influência é dos valores mais baixos da distribuição.") 

sns.histplot(precos_array, kde=True) # kde=True adiciona a curva de densidade, traduzindo seria "Kernel Density Estimate"
plt.title('Distribuição dos Preços dos Produtos')
plt.show()  

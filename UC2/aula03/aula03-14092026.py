# Aula 03- Dia 14/09/2026
# Tema principal: 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])
# print(dados)

# q1 = np.percentile(dados, 25)
# q2 = np.percentile(dados, 50)
# q3 = np.percentile(dados, 75)

# print(f"Primeiro quartil (Q1): {q1}")
# print(f"Segundo quartil (Q2, Mediana): {q2}")
# print(f"Terceiro quartil (Q3): {q3}")

df_transacoes = pd.read_excel('../exercicios/aula01/base_invest.xlsx', sheet_name='Transacoes')

print(df_transacoes.head(10))
# print(df_transacoes.tail())
# print(df_transacoes)

q1_preco = df_transacoes['preco'].quantile(0.25)
q2_preco = df_transacoes['preco'].quantile(0.50)
q3_preco = df_transacoes['preco'].quantile(0.75)

print(f"Primeiro quartil (Q1): {q1_preco}")
print(f"Segundo quartil (Q2, Mediana): {q2_preco}")
print(f"Terceiro quartil (Q3): {q3_preco}")

contagem_operacao = df_transacoes['operacao'].value_counts()

contagem_operacao.plot(kind='bar', title='Tipos de Operação')

plt.show()
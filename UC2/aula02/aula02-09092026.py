# Aula 02 - Dia 09/09/2026
# Tema principal: 

# LOC
# ILOC
# QUERY

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filmes = {
    'título': ["Lagoa Azul", "Agente Secreto", "Gênio Indomável", "A Freira", "Brinquedo Assassino", "Top Gun"],
    'categoria': ["Romance", "Ação", "Drama", "Terror", "Comédia", "Aventura"],
    'ano': ["1980", "2025", "1997", "2022", "1995", "1986"],
    'faturamento': [6.5, 4, 5.5, 3, 9, 7.2]
}

indices = ['A', 'B', 'C', 'D', 'E', 'F']

tabela_filmes = pd.DataFrame(filmes, indices)
print(tabela_filmes)

print('-'*60)
# print(tabela_filmes.iloc[0])
print(tabela_filmes.iloc[1:3])
print('-'*60)
# print(tabela_filmes.loc['B'])
print(tabela_filmes.loc['B':'E'])
print('-'*60)
consulta1 = tabela_filmes.query("faturamento == 6.5")
print(consulta1)
print('-'*60)

tabela_filmes.describe()

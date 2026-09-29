import pandas as pd
from statistic import calcular_medidas_descritivas, gerar_painel_boxplot

caminho_csv = "../aula03/vendas_produtos.csv" 

# 2. Carregar os dados
try:
    df = pd.read_csv(caminho_csv)

    precos_array = df['preco'].values
    
    medidas_calculadas = calcular_medidas_descritivas(precos_array)
    
    if medidas_calculadas:
        gerar_painel_boxplot(
            precos_array, 
            medidas_calculadas, 
            titulo_boxplot='Boxplot de Preços (vendas_produtos.csv)', 
            caminho_salvar='Relatorio_Precos.png'
        )

except FileNotFoundError:
    print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
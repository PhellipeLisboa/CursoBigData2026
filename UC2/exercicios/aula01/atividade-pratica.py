'''
Atividade Prática
Você recebeu um conjunto de dados de uma empresa de tecnologia voltada para aplicações
de investimentos. O objetivo é responder algumas perguntas importantes:
● Quais são as máximas e mínimas de operação de compra e venda das transações?
● Qual CNPJ tem o ativo de maior valor?
● Qual valor total em transações de cada participante?
Usando os conceitos de DataFrame e os comandos que aprendemos, crie um script que
carregue os dados e responda a essas perguntas.
'''

import pandas as pd


DISPLAY_WIDTH = 100


def print_separator(character, size):
    print(character * size)


df_transactions = pd.read_excel('base_invest.xlsx', 'Transacoes')
df_price_history = pd.read_excel('base_invest.xlsx', 'HistoricoPrecos')
df_asset = pd.read_excel('base_invest.xlsx', 'Ativo')
df_participant = pd.read_excel('base_invest.xlsx', 'Participante')

# print(df_transactions.head())
# print(df_price_history.head())
# print(df_asset.head())
# print(df_participant.head())

df_transactions_analysis = df_transactions.copy()

df_transactions_analysis['valor_total'] = (
    df_transactions_analysis['quantidade'] * df_transactions_analysis['preco']
)

purchase_transactions = df_transactions_analysis[df_transactions_analysis['operacao'] == 'compra']
sale_transactions = df_transactions_analysis[df_transactions_analysis['operacao'] == 'venda']

# Quais são as máximas e mínimas de operação de compra e venda das transações?

min_purchase_value = purchase_transactions['valor_total'].min()
max_purchase_value = purchase_transactions['valor_total'].max()
min_sale_value = sale_transactions['valor_total'].min()
max_sale_value = sale_transactions['valor_total'].max()

print_separator("=", DISPLAY_WIDTH)
print("Quais são as máximas e mínimas de operação de compra e venda das transações?".center(DISPLAY_WIDTH))
print_separator("=", DISPLAY_WIDTH)
print(
    f"O menor preço registrado nas operações de compra foi: R$ {min_purchase_value:.2f}")
print(
    f"O maior preço registrado nas operações de compra foi: R$ {max_purchase_value:.2f}")
print_separator("- ", DISPLAY_WIDTH // 2)
print(
    f"O menor preço registrado nas operações de venda foi: R$ {min_sale_value:.2f}")
print(
    f"O maior preço registrado nas operações de venda foi: R$ {max_sale_value:.2f}")


# Qual CNPJ tem o ativo de maior valor?

print_separator("=", DISPLAY_WIDTH)
print("Qual CNPJ tem o ativo de maior valor?".center(DISPLAY_WIDTH))
print_separator("=", DISPLAY_WIDTH)

latest_date = df_price_history['data'].max()

latest_price_history = df_price_history[df_price_history['data'] == latest_date]

highest_current_price = latest_price_history['preco'].max()

highest_current_price_rows = latest_price_history[
    latest_price_history['preco'] == highest_current_price
]

asset_id = highest_current_price_rows['id_ativo'].iloc[0]
data = highest_current_price_rows['data'].iloc[0]

asset_rows = df_asset[
    df_asset['id_ativo'] == asset_id
]

cnpj_with_highest_asset_value = asset_rows['cnpj'].iloc[0]

print(
    f"Na data mais recente do histórico, {data:%d/%m/%Y}, o CNPJ que possui o ativo de maior valor é: {cnpj_with_highest_asset_value}")
print(f"Valor do ativo nessa data: R$ {highest_current_price:.2f}")

# Qual valor total em transações de cada participante?

print_separator("=", DISPLAY_WIDTH)
print("Qual valor total em transações de cada participante?".center(DISPLAY_WIDTH))
print_separator("=", DISPLAY_WIDTH)


total_transactions_by_participant = (
    df_transactions_analysis.groupby('id_participante')['valor_total'].sum())

print("Total movimentado nas transações de cada participante:\n")

for participant_id, total_value in total_transactions_by_participant.items():
    print(f"Participante {participant_id}: R$ {total_value:.2f}")

print_separator("- ", DISPLAY_WIDTH // 2)


total_purchases_by_participant = (
    purchase_transactions.groupby('id_participante')['valor_total'].sum())

total_sales_by_participant = (sale_transactions.groupby(
    'id_participante')['valor_total'].sum())

net_cash_flow_by_participant = (
    total_sales_by_participant.sub(
        total_purchases_by_participant,
        fill_value=0
    )
)

print("Análise adicional: fluxo financeiro líquido de cada participante:\n")

for participant_id, net_cash_flow in net_cash_flow_by_participant.items():
    print(f"Participante {participant_id}: R$ {net_cash_flow:.2f}")

print_separator("=", DISPLAY_WIDTH)

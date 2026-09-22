import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="meu_ecommerce_novo"
)

cursor = conexao.cursor()

query = "SELECT * FROM produtos"
query2 = "SELECT p.id_pedido, c.nome AS nome_cliente, p.data_pedido, p.valor_total FROM pedidos p INNER JOIN clientes c ON p.id_cliente = c.id_cliente"
query3 = "SELECT p.id_pedido, c.nome AS cliente, pr.nome AS produto, p.quantidade, p.valor_total FROM pedidos p JOIN clientes c ON p.id_cliente = c.id_cliente JOIN produtos pr ON p.id_produto = pr.id_produto;"

cursor.execute(query3)   

# Obter os resultados
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

# Fechar a conexão
cursor.close()
conexao.close()

from listar_pedidos_da_mesa import listar_pedidos_da_mesa

# TESTES

pedidos = [
    {
        "numero_pedido": 101,
        "numero_mesa": 1,
        "id_garcom": 12,
        "itens": [
            {
                "codigo_prato": 1,
                "nome_prato": "Sushi de salmão",
                "preco_unitario": 24.90,
                "quantidade": 2,
                "observacoes": "Sem wasabi",
                "subtotal": 49.80,
            },
            {
                "codigo_prato": 2,
                "nome_prato": "Temaki",
                "preco_unitario": 18.00,
                "quantidade": 1,
                "observacoes": "",
                "subtotal": 18.00,
            },
            {
                "codigo_prato": 3,
                "nome_prato": "yakisoba",
                "preco_unitario": 21.50,
                "quantidade": 1,
                "observacoes": "",
                "subtotal": 43.00,
            },
        ],
        "status": "Aberto",
    },
    {
        "numero_pedido": 102,
        "numero_mesa": 1,
        "id_garcom": 12,
        "itens": [
            {
                "codigo_prato": 3,
                "nome_prato": "Ramen",
                "preco_unitario": 32.50,
                "quantidade": 2,
                "observacoes": "Sem cebolinha",
                "subtotal": 65.00,
            },
        ],
        "status": "Em preparo",
    },
    {
        "numero_pedido": 103,
        "numero_mesa": 2,
        "id_garcom": 8,
        "itens": [
            {
                "codigo_prato": 4,
                "nome_prato": "Yakisoba",
                "preco_unitario": 29.90,
                "quantidade": 1,
                "observacoes": "",
                "subtotal": 29.90,
            },
            {
                "codigo_prato": 5,
                "nome_prato": "Guioza",
                "preco_unitario": 15.00,
                "quantidade": 3,
                "observacoes": "Bem passado",
                "subtotal": 45.00,
            },
        ],
        "status": "Pronto",
    },
    {
        "numero_pedido": 104,
        "numero_mesa": 3,
        "id_garcom": 15,
        "itens": [],
        "status": "Aberto",
    },
    {
        "numero_pedido": 105,
        "numero_mesa": 1,
        "id_garcom": 12,
        "itens": [
            {
                "codigo_prato": 6,
                "nome_prato": "Hot roll",
                "preco_unitario": 22.00,
                "quantidade": 4,
                "observacoes": "Molho separado",
                "subtotal": 88.00,
            },
        ],
        "status": "Entregue",
    },
    {
        "numero_pedido": 106,
        "numero_mesa": 4,
        "id_garcom": 8,
        "itens": [
            {
                "codigo_prato": 7,
                "nome_prato": "Sashimi",
                "preco_unitario": 35.00,
                "quantidade": 2,
                "observacoes": "",
                "subtotal": 70.00,
            },
        ],
        "status": "Cancelado",
    },
]

result = listar_pedidos_da_mesa(1, pedidos)

print(result)

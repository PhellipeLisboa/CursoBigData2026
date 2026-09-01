
def listar_pedidos_da_mesa(numero_da_mesa, pedidos):
    '''
    Apresenta todos os pedidos de uma mesa.

    Retorna uma lista de pedidos e cada pedido é representado por um dicionário.
    '''

    pedidos_da_mesa = []
    
    for pedido in pedidos:

        if pedido['numero_da_mesa'] == numero_da_mesa:
            pedidos_da_mesa.append(pedido)

    print("=" * 60)
    print("RESTAURANTE TANOSHIMI - VISÃO DO GARÇOM".center(60))
    print("=" * 60)
    print(f"PEDIDOS DA MESA {numero_da_mesa}".center(60))
    print("=" * 60)

    indice_pedido = 0
    for pedido in pedidos_da_mesa:
        if indice_pedido != 0:
            print("-" * 60)
        print(f"PEDIDO {indice_pedido + 1}".center(60))
        print("-" * 60)

        for key in pedido:
            if key != 'numero_da_mesa':
                print(f"{key} - {pedido[key]}".center(60))

        indice_pedido += 1

    print("=" * 60)

    return pedidos_da_mesa
    

# TESTES 

'''
Estrutura da lista de pedidos
'''

pedidos = [
    {
        "numero_da_mesa": 1,
        "item": "Sushi",
        "quantidade": 2
    },
    {
        "numero_da_mesa": 1,
        "item": "Sushi 2",
        "quantidade": 4
    },
    {
        "numero_da_mesa": 2,
        "item": "Sushi 3",
        "quantidade": 8
    },
    {
        "numero_da_mesa": 1,
        "item": "Sushi 5",
        "quantidade": 1
    }
]

result = listar_pedidos_da_mesa(1, pedidos)

print(result)
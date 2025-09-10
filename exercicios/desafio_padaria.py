def dados() -> dict:
    '''Carregar e retornar os dados de produtos, fretes e funcionários'''
    return {
        'Atendente': 'Maria',
        'paes': {
            'frances': {'nome': 'Pão Francês', 'valor': 0.50, 'quantidade': 15},
            'doce': {'nome': 'Pão Doce', 'valor': 5.00, 'quantidade': 20},
            'forma': {'nome': 'Pão de Forma', 'valor': 5.99, 'quantidade': 18},
        },
        'bairros': {
            'barroco': {'nome': 'Barroco', 'frete': 5.00},
            'sao jose': {'nome': 'São José', 'frete': 15.00},
        },
        'codigo_venda_base': 95875,
    }

def obter_dados() -> dict:
    '''Solicitar e retornar os dados do cliente'''
    nome = input('Seu nome: ')
    return {'nome': nome}

def forma_pagamento() -> str:
    '''Solicitar e retornar a forma de pagamento escolhida'''
    while True:
        pagamento = input('Escolha a forma de pagamento (1-Dinheiro, 2-Cartão): ')
        if pagamento == '1':
            return 'Dinheiro'
        elif pagamento == '2':
            return 'Cartão'
        else:
            print('Forma de pagamento inválida')

def gerar_codigo(codigo_base: int) -> int:
    '''Gera e retorna o código de venda'''
    return codigo_base + 1

def calcula_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
    'Calcula o valor do frete com base no bairro de entrega'
    print('Bairro para entrega')
    while True:
        for bairro in bairros_disponiveis.values():
            print(f'- {bairro['nome']}')

        bairro_entrega = input('Qual o bairro para entregar? ').lower()

        bairro_encontrado = ''

        for chave, bairro in bairros_disponiveis.values():
            if bairro['nome'].lower() == bairro_entrega:
                bairro_encontrado = chave
                break

        if not bairro_encontrado:
            print('Bairro fora da área de entrega')
        else:
            frete = bairros_disponiveis[bairro_encontrado]['frete']
            return bairro_entrega, frete

def cadastrar_produto(estoque: dict) -> None:
    '''Permite ao atendente cadastrar um novo produto'''
    nome_produto = input('Digite o nome do novo produto (identificador): ').lower()

    if nome_produto in estoque:
        print('Erro! Produto ja cadastrado com este identificador')
        return
    try:
        nome_completo = input('Digite o nome completo do produto: ')
        valor = float(input('Digite o valor do novo produto: '))
        quantidade = int(input('Digite a quantidade inicial do produto: '))

        if nome_produto and nome_completo and valor > 0 and quantidade > 0:
            estoque[nome_produto] = {'nome': nome_completo, 'valor': valor, 'quantidade': quantidade}
            print(f'Produto {nome_completo} cadastrado com sucesso!')
        
        else:
            print('Erro! Dados inválidos')
    
    except ValueError:
        print('Entrada de dados inválida')

def atualizar_produto(estoque: dict) -> None:
    '''Permite ao atendente atualizar um produto existente'''
    nome_produto = input('Digite o nome do produto para atualizar (identificador): ').lower()

    if nome_produto not in estoque:
        print('Produto não cadastrado')
        return
    
    print(f'Produto '{estoque[nome_produto]}' selecionado')
    
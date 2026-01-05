def dados_produtos() -> dict:
    """Carregar e retornar os dados de produtos"""
    return {
        "paes": {
            "frances": {"nome": "Pão Francês", "valor": 0.50, "quantidade": 15},
            "doce": {"nome": "Pão Doce", "valor": 5.00, "quantidade": 20},
            "forma": {"nome": "Pão de Forma", "valor": 5.99, "quantidade": 18},
        },
    }


def dados_bairros() -> dict:
    """Carregar e retornar os dados de bairros e fretes"""
    return {
        "barroco": {"nome": "Barroco", "frete": 5.00},
        "sao jose": {"nome": "São José", "frete": 15.00},
    }


def dados_funcionarios() -> dict:
    """Carregar e retornar dados de funcionários"""
    return {"Atendente": "Maria"}


def obter_nome_cliente() -> dict:
    """Solicitar e retornar os dados do cliente (nome)"""
    nome = input("Seu nome: ")
    return {"nome": nome}


def escolher_forma_pagamento() -> str:
    """Solicitar e retornar a forma de pagamento escolhida"""
    while True:
        pagamento = input("Escolha a forma de pagamento (1-Dinheiro, 2-Cartão): ")
        if pagamento == "1":
            return "Dinheiro"
        elif pagamento == "2":
            return "Cartão"
        else:
            print("Forma de pagamento inválida")


def gerar_codigo_venda(codigo_base: int) -> int:
    """Gera e retorna o código de venda com base em um código base"""
    return codigo_base + 1


def listar_bairros_disponiveis(bairros_disponiveis: dict):
    """Exibe a lista de bairros disponíveis para entrega"""
    for bairro in bairros_disponiveis.values():
        print(f'- {bairro["nome"]}')


def obter_bairro_entrega(bairros_disponiveis: dict) -> tuple[str, float] | None:
    """Solicita o bairro de entrega e retorna o bairro e o frete, ou None se inválido"""
    print("Bairro para entrega")
    while True:
        listar_bairros_disponiveis(bairros_disponiveis)
        bairro_entrega = input("Qual o bairro para entregar? ").lower()

        for chave, bairro in bairros_disponiveis.items():
            if bairro["nome"].lower() == bairro_entrega:
                return bairro_entrega, bairro["frete"]

        print("Bairro fora da área de entrega")


def cadastrar_produto(estoque: dict) -> None:
    """Solicita os dados e cadastra um novo produto"""
    nome_produto = input("Digite o nome do novo produto (identificador): ").lower()

    if nome_produto in estoque:
        print("Erro! Produto já cadastrado com este identificador")
        return

    nome_completo = input("Digite o nome completo do produto: ")
    valor = solicitar_valor_produto()
    quantidade = solicitar_quantidade_produto()

    if nome_produto and nome_completo and valor > 0 and quantidade > 0:
        estoque[nome_produto] = {
            "nome": nome_completo,
            "valor": valor,
            "quantidade": quantidade,
        }
        print(f"Produto {nome_completo} cadastrado com sucesso!")
    else:
        print("Erro! Dados inválidos")


def solicitar_valor_produto() -> float:
    """Solicita o valor do produto e retorna, tratando erro de entrada"""
    while True:
        try:
            valor = float(input("Digite o valor do novo produto: "))
            if valor > 0:
                return valor
            else:
                print("Valor inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.")


def solicitar_quantidade_produto() -> int:
    """Solicita a quantidade do produto e retorna, tratando erro de entrada"""
    while True:
        try:
            quantidade = int(input("Digite a quantidade inicial do produto: "))
            if quantidade > 0:
                return quantidade
            else:
                print("Quantidade inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


def atualizar_produto(estoque: dict) -> None:
    """Permite ao atendente atualizar um produto existente"""
    nome_produto = input(
        "Digite o nome do produto para atualizar (identificador): "
    ).lower()

    if nome_produto not in estoque:
        print("Produto não cadastrado")
        return

    produto = estoque[nome_produto]
    print(f'Produto "{produto["nome"]}" selecionado para atualização.')


def main():
    # Carregar dados
    produtos = dados_produtos()
    bairros = dados_bairros()
    funcionario = dados_funcionarios()

    # Obter dados do cliente
    cliente = obter_nome_cliente()

    # Escolher forma de pagamento
    pagamento = escolher_forma_pagamento()

    # Gerar código de venda
    codigo_venda = gerar_codigo_venda(95875)
    print(f"\nCódigo da venda gerado: {codigo_venda}")

    # Calcular frete
    bairro_entrega, frete = obter_bairro_entrega(bairros)
    if bairro_entrega:
        print(f"Frete para o bairro {bairro_entrega}: R${frete:.2f}")

    # Mostrar produtos disponíveis
    print("\nProdutos disponíveis:")
    for chave, produto in produtos["paes"].items():
        print(
            f"{produto['nome']} - R${produto['valor']:.2f} (Quantidade: {produto['quantidade']})"
        )

    # Exemplo de cadastro de produto (para o atendente)
    print("\nCadastro de um novo produto:")
    cadastrar_produto(produtos["paes"])

    # Exemplo de atualização de produto (para o atendente)
    print("\nAtualização de produto:")
    atualizar_produto(produtos["paes"])


if __name__ == "__main__":
    main()

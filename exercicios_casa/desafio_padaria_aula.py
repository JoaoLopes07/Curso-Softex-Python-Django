nome_frances = "frances"
nome_doce = "doce"
nome_forma = "forma"

valor_frances = 0.50
valor_forma = 5.99
valor_doce = 5.00

quantidade_frances = 15
quantidade_forma = 18
quantidade_doce = 20

atendente = "Maria"

bairro_barroco = "barroco"
bairro_saojose = "sao jose"

frete_barroco = 5.00
frete_saojose = 15.00

codigo_venda = 1

while True:
    print(f"-- Bem Vindo a Padaria Desespero. Sou a atendente {atendente} --\n")
    escolha = input(
        f"Temos os pães: {nome_frances, nome_forma, nome_doce}\nDigite qual você quer: "
    ).lower()
    if escolha == nome_frances:
        quantidade = int(input("Digite a quuantidade de pães: "))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido = quantidade
            valor_compra = quantidade * valor_frances
            print(f"Seu pedido ficou em R$ {valor_compra}")
        else:
            print(f"Infelizmente só tenho {quantidade_frances} no momento")
            break
    entrega = input("Digite 1 para retirar e 2 para entregar").lower()
    if entrega == "2":
        bairro_entrega = input(
            f"Qual o bairro? (1:{bairro_saojose},2:{bairro_barroco})"
        )
        if bairro_entrega == "1":
            valor_frete = frete_barroco
            print(f"Valor do frete R$ {valor_frete}")
        elif bairro_entrega == "2":
            valor_frete = frete_saojose
            print(f"Valor do frete R$ {valor_frete}")
        else:
            print("Fora da área de entrega")
            break
    elif entrega == "1":
        valor_frete = 0.00
    else:
        print("Número Inválido")
        break

    dados_cliente = input("Informe o seu nome: ")
    forma_de_pagamento = input(
        "Escolha a forma de pagamento (1: Dinheiro, 2: Cartão): "
    )

    if forma_de_pagamento == "1":
        forma_de_pagamento = "Dinheiro"
    else:
        forma_de_pagamento = "Cartão"

    codigo_atual = codigo_venda + 1

    print(f"O valor total da sua compra foi de R$ {valor_compra + valor_frete}")
    break

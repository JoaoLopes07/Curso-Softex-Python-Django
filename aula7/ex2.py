class Hamburguer:
    def pedido(self):
        preco_hamburguer = 19.99
        cupom = "desconto"
        nome_hamburguer = "hamburguer"

        while True:
            pedido = input("Digite o nome do hambúrguer desejado: ").lower()
            if pedido == nome_hamburguer:
                print(f"Valor do hamburguer: {preco_hamburguer}")
                break
            else:
                print("Nome Inválido")

        while True:
            desconto = input(
                "Você tem um cupom de desconto? Digite apenas (sim) ou (nao): "
            ).lower()
            if desconto == "sim":
                nome_cupom = input("Digite o cupom: ").lower()

                if nome_cupom == cupom:
                    print("Você ganhou 5% de desconto")
                    print(
                        f"Pedido Finalizado.\nValor total = {preco_hamburguer - (preco_hamburguer * 0.05):.2f}"
                    )
                    break
                elif nome_cupom != cupom:
                    print("Cupom Inválido")

            elif desconto == "nao":
                print(f"Pedido Finalizado.\nValor total = {preco_hamburguer}")
                break

            else:
                print("Resposta Inválida")


rodar = Hamburguer()

rodar.pedido()

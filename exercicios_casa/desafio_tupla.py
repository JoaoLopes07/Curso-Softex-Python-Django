'''Sua tarefa é processar um fluxo de dados de acessos de usuários, identificando informações importantes e tratando possíveis erros. O programa deve pedir ao usuário para inserir dados de acesso, que consistem em um nome de usuário, um status de acesso e um número que representa a duração da sessão em minutos. O usuário pode inserir quantos acessos quiser. Para parar a inserção de dados, ele deve digitar "parar". Objetivo: 1. Armazene cada acesso válido como uma tupla (usuário, status, duracao_minutos). 2. Adicione essas tuplas a uma lista chamada registros_acessos. 3. Use um conjunto para armazenar todos os usuários que tiveram pelo menos um acesso bem-sucedido. 4. No final, calcule e imprima o tempo total de todas as sessões bem-sucedidas.'''

class GerenciadorAcessos:
    def __init__(self):
        self.registros = []
        self.usuarios_sucesso = set()
        self.tempo_total = 0

    def adicionar_acesso(self, usuario, status, duracao):
        self.registros.append((usuario, status, duracao))

        if status == "sucesso":
            self.usuarios_sucesso.add(usuario)
            self.tempo_total += duracao

    def resultados(self):
        print("\nRESULTADOS FINAIS")
        print("Registros de acessos:")
        print(self.registros)

        print("\nUsuários com acesso bem-sucedido:")
        print(self.usuarios_sucesso)

        print(f"\nTempo total das sessões bem-sucedidas: {self.tempo_total} minutos")

    def loop(self):
        while True:
            usuario = input("Digite o nome de usuário (ou 'parar' para sair): ").strip()
            if usuario.lower() == "parar":
                break

            print("Selecione o status:\n1 - Sucesso\n2 - Falha")
            opcao = input("Opção: ")

            if opcao not in ["1", "2"]:
                print("Opção inválida!\n")
                continue

            status = "sucesso" if opcao == "1" else "falha"

            try:
                duracao = int(input("Digite a duração da sessão em minutos: "))
            except ValueError:
                print("Valor inválido para duração.\n")
                continue

            self.adicionar_acesso(usuario, status, duracao)

        self.resultados()


rodar = GerenciadorAcessos()
rodar.loop()

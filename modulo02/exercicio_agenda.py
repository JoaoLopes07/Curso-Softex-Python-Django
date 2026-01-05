class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self):
        nome = input("Digite o nome do contato para salvar: ").lower()
        telefone = input("Telefone: ")
        self.contatos[nome] = telefone
        print("Contato adicionado!\n")

    def buscar_contato(self):
        buscar = input("Qual contato você quer buscar? ").lower()
        if buscar in self.contatos:
            print("Contato encontrado:", {buscar: self.contatos[buscar]})
        else:
            print("Esse contato não existe\n")

    def menu(self):
        while True:
            print(
                "--Menu de Opções--\nDigite 1 para adicionar contato\nDigite 2 para buscar contato\nDigite 3 para sair\n"
            )

            opcao = input("Opção: ")

            if opcao == "1":
                self.adicionar_contato()
            elif opcao == "2":
                self.buscar_contato()
            elif opcao == "3":
                print("Encerrando...")
                break
            else:
                print("Opção Inválida\n")


rodar = Agenda()
rodar.menu()

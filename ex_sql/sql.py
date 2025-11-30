import sqlite3
import os

NOME_BANCO = 'loja.db'

def criar_conexao():
    """Cria conexão com o banco e habilita chaves estrangeiras"""
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def main():
    # Garante um ambiente limpo para o teste, recriando o banco
    if os.path.exists(NOME_BANCO):
        os.remove(NOME_BANCO)

    conexao = criar_conexao()
    cursor = conexao.cursor()
    
    print("Iniciando processamento do banco de dados...")

    # 1. Estrutura das Tabelas (DDL)
    cursor.execute("""
    CREATE TABLE Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE Produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE Pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_compra DATETIME DEFAULT CURRENT_TIMESTAMP,
        total REAL,
        id_cliente INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE Itens_Pedido (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id),
        FOREIGN KEY (id_produto) REFERENCES Produtos(id)
    );
    """)
    print("Tabelas criadas com sucesso.")

    # 2. Insercao de Dados
    cursor.executemany("INSERT INTO Clientes (nome, email) VALUES (?, ?)", [
        ('Joao', 'joao@email.com'),
        ('Maria', 'maria@email.com'),
        ('Ana', 'ana@email.com')
    ])

    cursor.executemany("INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)", [
        ('Teclado Mecanico', 150.00, 50),
        ('Mouse Gamer', 50.00, 100),
        ('Monitor 24 Pol', 850.00, 20)
    ])

    # Criando pedido para Maria (ID 2)
    cursor.execute("INSERT INTO Pedidos (id_cliente, total) VALUES (?, ?)", (2, 250.00))
    id_pedido = cursor.lastrowid

    # Inserindo itens no pedido (1 Teclado e 2 Mouses)
    cursor.executemany("INSERT INTO Itens_Pedido (id_pedido, id_produto, quantidade) VALUES (?, ?, ?)", [
        (id_pedido, 1, 1),
        (id_pedido, 2, 2)
    ])
    
    conexao.commit()
    print("Dados iniciais inseridos.")

    # 3. Consultas (Read)
    print("\n--- Relatorio: Produtos acima de R$ 100 ---")
    cursor.execute("SELECT nome, preco FROM Produtos WHERE preco > 100.00")
    for linha in cursor.fetchall():
        print(f"Produto: {linha[0]} | Preco: R$ {linha[1]:.2f}")

    print("\n--- Relatorio: Historico de Pedidos (Cliente: Maria) ---")
    cursor.execute("""
        SELECT Clientes.nome, Pedidos.id, Pedidos.data_compra 
        FROM Clientes 
        JOIN Pedidos ON Clientes.id = Pedidos.id_cliente 
        WHERE Clientes.nome = 'Maria'
    """)
    for linha in cursor.fetchall():
        print(f"Cliente: {linha[0]} | Pedido ID: {linha[1]} | Data: {linha[2]}")

    # 4. Atualizacoes (Update)
    print("\nAtualizando precos e estoque...")
    cursor.execute("UPDATE Produtos SET preco = preco * 1.10 WHERE nome = 'Mouse Gamer'")
    cursor.execute("UPDATE Produtos SET estoque = estoque - 2 WHERE nome = 'Mouse Gamer'")
    conexao.commit()

    # 5. Remocoes (Delete)
    print("Removendo registros obsoletos...")
    cursor.execute("DELETE FROM Clientes WHERE nome = 'Joao'")
    cursor.execute("DELETE FROM Itens_Pedido WHERE id_pedido = ? AND id_produto = 1", (id_pedido,))
    conexao.commit()

    conexao.close()
    print("\nProcesso finalizado com sucesso.")

if __name__ == "__main__":
    main()
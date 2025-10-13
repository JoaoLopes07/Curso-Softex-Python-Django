import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel:
    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()
    
    def _create_table(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            '''
            CREATE TABLE blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_user INTEGER NOT NULL,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
            );'''
        )
        self.db_conn.close()
    
    def create_postagem(self, titulo, conteudo):
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO blogs (titulo, conteudo)
                VALUES (?, ?);
            """,
                (titulo, conteudo),
            )
            print("Postagem realizada com sucesso!")
        finally:
            self.db_conn.close()

    def get_all_postagens(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs;")
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts
    
    def find_postagens_by_id(self, id):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs WHERE id = ?;", (id,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user
    
    def find_postagens_by_id_user(self, id_user):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs WHERE id_user = ?;", (id_user,))
        user = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return user
    
    def update_posts_by_id(self, id, titulo=None, conteudo=None):
        self.db_conn.connect()
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)

        if not updates:
            print("Nenhuma postagem para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(id)

        query = f"UPDATE blogs SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Postagem atualizada com sucesso!")
        self.db_conn.close()
    
    def delete_user_by_id(self, id):
        """Deleta uma Postagem pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM usuarios WHERE id = ?;", (id,))
        print("Postagem deletada com sucesso!")
        self.db_conn.close()
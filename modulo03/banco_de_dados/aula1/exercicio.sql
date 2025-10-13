-- Active: 1759754148311@@127.0.0.1@3306
create table usuarios (
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);
create table postagens (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER NOT NULL,
    Foreign Key (id_autor) REFERENCES usuarios(id)
);

SELECT * FROM usuarios;
SELECT * FROM postagens;

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Anderson', 'Cachinhos Dourados', 'anderson@gmail.com', 'anderson123')

INSERT INTO postagens (titulo, postagem, id_autor) VALUES ('Almoço com Douglas', 'Tive um encontro com Douglas', 5)

-- Active: 1759754148311@@127.0.0.1@3306
create table alunos (
    id integer primary key,
    nome text not null,
    idade integer
);

insert into alunos (nome, idade) values ('João', 20);
insert into alunos (nome, idade) values ('Maria', 22);

select * from alunos;

select nome, idade from alunos;

select * from alunos where idade = 20;

select * from alunos where nome = 'Maria' and idade = 22;

update alunos set idade = 21 where nome = 'João';
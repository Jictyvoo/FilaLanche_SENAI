create database if not exists Fila_Lanche_SENAI;

use Fila_Lanche_SENAI;

CREATE TABLE if not exists Produto (
id_produto int not null auto_increment,
nome varchar(70),
preco float not null,
quantidade int,
PRIMARY KEY(id_produto)
);

CREATE TABLE if not exists Sala_Horario (
id_sala int not null auto_increment,
nome_sala varchar(30) not null,
ocupado varchar(30),
noite time,
manha time,
tarde time,
PRIMARY KEY(id_sala)
);

CREATE TABLE if not exists Estudante (
matricula int not null auto_increment,
id_sala int,
nome varchar(70) not null,
data_nascimento date not null,
turma varchar(30) not null,
PRIMARY KEY(matricula),
FOREIGN KEY(id_sala) REFERENCES Sala_Horario(id_sala)
);

CREATE TABLE if not exists Pedido (
id_produto int not null,
matricula int not null,
data_horario datetime not null,
quantidade int not null,
FOREIGN KEY(id_produto) REFERENCES Produto(id_produto),
FOREIGN KEY(matricula) REFERENCES Estudante(matricula)
);

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

CREATE TABLE if not exists Pessoa (
id_pessoa int not null auto_increment,
cpf int(11),
password varchar(40),
rg int(10),
nome varchar(70) not null,
data_nascimento date not null,
PRIMARY KEY(id_pessoa)
);

CREATE TABLE if not exists Turma(
id_turma int not null auto_increment,
nome varchar(30) not null,
PRIMARY KEY(id_turma)
);

CREATE TABLE if not exists Estudante (
id_estudante int not null auto_increment,
id_pessoa int not null,
id_sala int,
id_turma int,
PRIMARY KEY(id_estudante),
FOREIGN KEY(id_pessoa) REFERENCES Pessoa(id_pessoa),
FOREIGN KEY(id_sala) REFERENCES Sala_Horario(id_sala),
FOREIGN KEY(id_turma) REFERENCES Turma(id_turma)
);

CREATE TABLE if not exists Administrador (
id_administrador int not null auto_increment,
id_pessoa int not null,
cargo varchar(40),
matricula int,
PRIMARY KEY(id_administrador),
FOREIGN KEY(id_pessoa) REFERENCES Pessoa(id_pessoa)
);

CREATE TABLE if not exists Pedido (
id_produto int not null,
id_estudante int not null,
data_horario datetime not null,
quantidade int not null,
FOREIGN KEY(id_produto) REFERENCES Produto(id_produto),
FOREIGN KEY(id_estudante) REFERENCES Estudante(id_estudante)
);

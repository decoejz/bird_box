DROP DATABASE IF EXISTS bird_box;
CREATE DATABASE bird_box;
USE bird_box;

CREATE TABLE usuario (
    nome VARCHAR(30) NOT NULL,
    email VARCHAR(40) NOT NULL,
    cidade VARCHAR(40) NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE passaro (
    nome VARCHAR(30) NOT NULL,
    PRIMARY KEY (nome)
);

CREATE TABLE preferencia(
	email VARCHAR(40) NOT NULL,
    nome VARCHAR(30) NOT NULL,
    PRIMARY KEY (email, nome),
	FOREIGN KEY (email)
		REFERENCES usuario(email),
	FOREIGN KEY (nome)
		REFERENCES passaro(nome)
);

CREATE TABLE post(
	id INT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(40) NOT NULL,
    texto VARCHAR(300),
    url VARCHAR(100),
    ativo INT NOT NULL DEFAULT 1,
    email VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (email)
		REFERENCES usuario(email)
);

CREATE TABLE usuario_post(
	email VARCHAR(40) NOT NULL,
    id INT NOT NULL,
    ativo INT NOT NULL DEFAULT 1,
    PRIMARY KEY (email, id),
	FOREIGN KEY (email)
		REFERENCES usuario(email),
	FOREIGN KEY (id)
		REFERENCES post(id)
);

CREATE TABLE tag_usuario(
	email VARCHAR(40) NOT NULL,
    id INT NOT NULL,
    ativo INT NOT NULL DEFAULT 1,
    PRIMARY KEY (email, id),
	FOREIGN KEY (email)
		REFERENCES usuario(email),
	FOREIGN KEY (id)
		REFERENCES post(id)
);

CREATE TABLE tag_passaro(
	nome VARCHAR(40) NOT NULL,
    id INT NOT NULL,
    ativo INT NOT NULL DEFAULT 1,
    PRIMARY KEY (nome, id),
	FOREIGN KEY (nome)
		REFERENCES passaro(nome),
	FOREIGN KEY (id)
		REFERENCES post(id)
);

CREATE TABLE usuario_viu(
	email VARCHAR(40) NOT NULL,
    id INT NOT NULL,
    so VARCHAR(20),
    ip VARCHAR(15),
	browser VARCHAR(20),
    visto_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ativo INT NOT NULL DEFAULT 1,
    PRIMARY KEY (email, id),
	FOREIGN KEY (email)
		REFERENCES usuario(email),
	FOREIGN KEY (id)
		REFERENCES post(id)
);
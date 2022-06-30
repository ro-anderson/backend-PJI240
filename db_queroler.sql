CREATE DATABASE IF NOT EXISTS queroler_db;
USE queroler_db;
CREATE TABLE IF NOT EXISTS doadores (
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(30) NOT NULL,
    PRIMARY KEY(nome)
);
INSERT INTO doadores (nome, email) VALUES
("Rodrigo Didier Anderson", "didier.rda@gmail.com");

CREATE DATABASE bycoders;
\c bycoders;

CREATE TABLE IF NOT EXISTS cnab(
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(22) NOT NULL,
    data DATE NOT NULL,
    valor FLOAT NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    cartao VARCHAR(12) NOT NULL,
    hora TIME NOT NULL
);
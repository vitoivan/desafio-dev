CREATE DATABASE bycoders WITH ENCODING 'UTF8';
\c bycoders;

CREATE TABLE IF NOT EXISTS donos(
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(14) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS lojas(
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(19) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS tipos(
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(22) NOT NULL
);

INSERT INTO tipos
    (nome)
VALUES
    ('Débito'),
    ('Boleto'),
    ('Financiamento'),
    ('Crédito'),
    ('Recebimento Empréstimo'),
    ('Vendas'),
    ('Recebimento TED'),
    ('Recebimento DOC'),
    ('Aluguel');

CREATE TABLE IF NOT EXISTS transacoes(
    id SERIAL PRIMARY KEY,
    tipo_id INTEGER NOT NULL REFERENCES tipos(id),
    data DATE NOT NULL,
    valor FLOAT NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    cartao VARCHAR(12) NOT NULL,
    hora TIME NOT NULL,
    id_dono INTEGER NOT NULL REFERENCES donos(id),
    id_loja INTEGER NOT NULL UNIQUE REFERENCES lojas(id)
);

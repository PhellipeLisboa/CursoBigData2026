-- CRIANDO O BANCO DE DADOS

CREATE DATABASE meu_ecommerce_test;

USE meu_ecommerce_test;

-- CRIANDO A ENTIDADE PRODUTOS:

CREATE TABLE Produtos (
	id_produto VARCHAR(10),
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(8,2),
    estoque INT 
);

-- CRIANDO A ENTIDADE CLIENTES:

CREATE TABLE Clientes (
	id_cliente VARCHAR(10),
    nome VARCHAR(100),
    email VARCHAR(30)
);

-- CRIANDO A ENTIDADE PEDIDOS:

CREATE TABLE Pedidos (
	id_pedido VARCHAR(10),
    id_cliente VARCHAR(10),
    data_pedido DATETIME,
    valor_total DECIMAL(10,2),
    id_produto VARCHAR(10),
    quantidade SMALLINT
)

-- VISUALIZAR AS ENTRADAS DAS TABELAS APÓS INJEÇÃO DE DADOS

SELECT * FROM Produtos;

SELECT * FROM Clientes;

SELECT * FROM Pedidos;

-- CRIAÇÃO DE CHAVES PRIMÁRIAS

ALTER TABLE produtos
ADD CONSTRAINT pk_produto
PRIMARY KEY (id_produto);

ALTER TABLE clientes
ADD CONSTRAINT pk_cliente
PRIMARY KEY (id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT pk_pedidos
PRIMARY KEY (id_pedido);

-- RELACIONANDO AS TABELAS POR MEIO DAS CHAVES ESTRANGEIRAS

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_produtos
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

-- EXEMPLOS DE DQL

SELECT nome, preco
FROM produtos
ORDER BY preco DESC;

SELECT *
FROM produtos
WHERE categoria = 'Eletrônicos' AND preco > 1000;

SELECT *
FROM produtos
WHERE categoria = 'Eletrônicos' OR categoria = 'Saúde';

SELECT *
FROM produtos
WHERE nome LIKE 'Smartphone%';

SELECT *
FROM clientes
WHERE email NOT LIKE '%@email.com';

SELECT *
FROM produtos
WHERE nome LIKE '%GAMER%';

SELECT *
FROM clientes 
WHERE nome like '_ia';

SELECT c.nome, p.data_pedido
FROM clientes c
JOIN pedidos p	ON c.id_cliente = p.id_cliente;

SELECT 
	COUNT(*) AS total_pedidos,
    SUM(valor_total) AS faturamento_total,
    AVG(valor_total) AS ticket_medio
FROM pedidos;

SELECT categoria, COUNT(*) AS qtd_produtos, AVG(preco) AS preco_medio
FROM produtos
GROUP BY categoria
HAVING qtd_produtos > 5;

-- DROP TABLE Produtos;

-- INJEÇÃO DE DADOS ATRAVÉS DE CÓDIGO SQL

-- SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- -- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

-- LOAD DATA LOCAL INFILE 'C:\\Users\\phellipe.barbosa\\Documents\\BIGDATA\\CursoBigData2026\\UC2\\aula03\\vendas_produtos.csv' -- Ajuste o caminho no seu banco local
-- INTO TABLE meu_ecommerce_test.Produtos
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\r\n' -- Aqui: CR LF
-- IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
-- (id_produto, nome, categoria, @preco_var, estoque) -- Mapeia colunas
-- SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente

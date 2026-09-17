-- CREATE DATABASE teste;

USE teste;

-- CRIANDO A ENTIDADE PRODUTOS:

CREATE TABLE Produtos (
	id_produto VARCHAR(10),
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(8,2),
    estoque INT 
);

SELECT * FROM Produtos;

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE 'C:\\Users\\phellipe.barbosa\\Documents\\BIGDATA\\CursoBigData2026\\UC2\\aula03\\vendas_produtos.csv' -- Ajuste o caminho no seu banco local
INTO TABLE teste.Produtos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_produto, nome, categoria, @preco_var, estoque) -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente

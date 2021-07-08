INSERT INTO hotel (nome, cidade, cap_hotel, endereco)
VALUES 	('Uruguai', 'Curitiba', 10, 'rua 1, num123'),
		('Brasil', 'Florianopolis', 15, 'rua 2, num234'),
		('Argentina', 'Natal', 8, 'rua 3, num345'),
		('Canada', 'João Pessoa', 10, 'rua 4, num456'),
		('França', 'Caruaru', 8, 'rua 5, num567');

select * from hotel

INSERT INTO telefone (id_hotel, telefone)
VALUES 	(1, 55555555),(2, 02020202),(2, 0101010101),(3, 99955959),(4, 458799888),(4, 857485472),(5, 0554599945),(5, 88990000),(2, 438795103),
		(1, 44444444);
		
select * from telefone inner join hotel on telefone.id_hotel = hotel.id_hotel

INSERT INTO habitacao (numero, valor, capacidade, categoria, id_hotel)
VALUES 	(101, 170, 2, 'standar', 2), (102, 170, 2, 'standar', 2), (103, 120, 3, 'economica', 2), (104, 120, 3, 'economica', 2), (201, 90, 1, 'standar', 2),
        (202, 120, 1, 'standar', 2), (203, 200, 2, 'premium', 2), (204, 150, 1, 'premium', 2), (301, 250, 2, 'premium', 2), (302, 300, 2, 'premium', 2),
        (303, 120, 1, 'standar', 2), (304, 200, 2, 'premium', 2), (401, 150, 1, 'premium', 2), (403, 250, 2, 'premium', 2), (402, 300, 2, 'premium', 2)
;

select * from habitacao


INSERT INTO articulo_servico (nome, preco, tipo, descricao)
VALUES ('coca-cola',10,'articulo','600mm'), ('coca-cola',12,'articulo','1.5litros'), ('coca-cola',15,'articulo','2litros'),
('guarana',8,'articulo','600mm'),('guarana',10,'articulo','1.5litros'),('guarana',12,'articulo','2litros'),
('bolo',15,'articulo','chocolate'),('bolo',15,'articulo','vainilha'),('bolo',15,'articulo','zanhaoria'),
('Protetor solar',50,'articulo','FPS 50'),('Protetor solar',70,'articulo','FPS 65'),
('Paseio',150,'serviço','Paseio pela cidade'),('lavagem de roupas',50,'serviço','lavagem normal'),('lavagem de roupas',75,'serviço','lavagem forte'),
('aluguel de bike',40,'serviço','aluguel por 4 horas'),('aluguel de bike',60,'serviço','aluguel pelo dia todo')
;
CREATE TABLE Hotel (
  Id_hotel SERIAL,
  Nome varchar(50) NOT NULL,
  Cidade varchar(50) NOT NULL,
  Cap_Hotel varchar(50) NOT NULL,
  Endereco varchar(100) NOT NULL,
  url_img TEXT,
  PRIMARY KEY (Id_hotel)
);


CREATE TABLE telefone (
  id_hotel int NOT NULL,
  telefone int,
  PRIMARY KEY (Telefone)
);


CREATE TABLE empregado 
(
  cpf int PRIMARY KEY,
  nome varchar(50) NOT NULL,
  sobrenome varchar(50) NOT NULL,
  telefone int NOT NULL,
  endereco varchar(100) DEFAULT NULL,
  nome_usuario varchar(50) NOT NULL,
  senha varchar(50) NOT NULL,
  cargo varchar(50) NOT NULL,
  id_hotel int NOT NULL REFERENCES hotel (id_hotel)
)
;

CREATE TABLE cliente (
  id_cliente SERIAL NOT NULL,
  cpf int DEFAULT NULL,
  pasaporte int DEFAULT NULL,
  nome varchar(50) NOT NULL,
  sobrenome varchar(50) NOT NULL,
  telefone int NOT NULL,
  endereco varchar(100),
  saldo decimal(10,2) NOT NULL,
  id_hotel int NOT NULL REFERENCES hotel (id_hotel) ,
  procedencia varchar(20) DEFAULT 'Brasil',
  vip boolean DEFAULT FALSE,
  PRIMARY KEY (id_cliente)
);

CREATE TABLE articulo_servico (
  codigo SERIAL,
  nome varchar(50) NOT NULL,
  preco decimal(10,2) NOT NULL,
  tipo varchar(10) NOT NULL,
  descricao text DEFAULT NULL,
  url_img TEXT,
  PRIMARY KEY (codigo)
);

CREATE TABLE habitacao (
  id_hab SERIAL,
  numero int NOT NULL,
  valor decimal(10,2) NOT NULL,
  capacidade int NOT NULL,
  categoria varchar(50) NOT NULL,
  id_hotel int NOT NULL REFERENCES hotel (id_hotel),
  estado boolean DEFAULT FALSE,
  PRIMARY KEY (id_hab)
);


CREATE TABLE Reserva (
  Num_reserva int PRIMARY KEY,
  Data_in date NOT NULL,
  Data_out date NOT NULL,
  Vip boolean DEFAULT FALSE,
  Id_cliente int NOT NULL REFERENCES Cliente (Id_cliente)
);

CREATE TABLE Hab_res (
  Num_res int NOT NULL REFERENCES Reserva (Num_reserva),
  id_hab int NOT NULL REFERENCES Habitacao (id_hab),
  Data_res date NOT NULL,
  Id_hotel int NOT NULL REFERENCES Hotel (Id_hotel)
);

CREATE TABLE Faturacao (
  Nota_num serial,
  Numero_res int NOT NULL REFERENCES Reserva (Num_reserva),
  Saldo_cliente int NOT NULL,
  Forma_pago varchar(30) NOT NULL,
  Data_nota date NOT NULL,
  Id_hotel int NOT NULL REFERENCES hotel (id_hotel),
  Valor_nota int NOT NULL,
  PRIMARY KEY (Nota_num)
);

CREATE TABLE Consumo (
  Num_venda serial NOT NULL,
  Cod_art_serv int NOT NULL REFERENCES Articulo_Servico (Codigo),
  Data_venda date NOT NULL,
  Num_hab int NOT NULL,
  Num_res int NOT NULL REFERENCES Reserva (Num_reserva),
  Id_hotel int NOT NULL REFERENCES Hotel (Id_hotel),
  PRIMARY KEY (Num_venda)
);






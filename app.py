from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)


#Configuracoes de acceso ao banco de dados
user = 'nzygbpdp'
password = 'lqxrDV6TMksZJl5ZoSbWji9PD0hETYGB'
host = 'tuffi.db.elephantsql.com'
database = 'nzygbpdp'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "pepe pepe pepe"

#Intanciando objeto da Classe SQLAlchemy 
db = SQLAlchemy(app)

#-----------------------------------------------  Classe Reserva -------------------------------------------------

class Reserva(db.Model):
    num_reserva = db.Column(db.Integer, primary_key=True)
    data_in = db.Column(db.Date, nullable=False)
    data_out = db.Column(db.Date, nullable=False)
    id_cliente = db.Column(db.Integer, nullable=False)

    def __init__(self, num_reserva, data_in, data_out, id_cliente):
        self.num_reserva = num_reserva
        self.data_in = data_in
        self.data_out = data_out
        self.id_cliente = id_cliente
    

        @staticmethod
        def reserva_read_all()():

            # SELECT * from filmes ORDER BY id ASC
            all_reserva = Reserva.query.order_by(Habitacao.id_hab.asc()).all()
            output = []
            for reserva in all_reserva:   
                salida = {}
                salida['num_res'] = reserva.num_res
                salida['numero'] = reserva.Data_in
                salida['valor'] = reserva.Data_out
                salida['capacidade'] = reserva.id_cliente
                output.append(salida)
            all_cliente = Cliente.
            return output
    
    @staticmethod
    def delete():
        db.session.delete()
        db.session.commit()
    
    @staticmethod
    def read_id(numeroReserva):
        return db.query.get(numeroReserva)

    @staticmethod
    def update(data_in, data_out):
        data_in = data_in
        data_out = data_out


#-----------------------------------------------  Casse Hab_Res -------------------------------------------------

class hab_res(db.Model):
    __tablename__= "hab_res"
    num_res = db.Column(db.Integer, nullable=False)
    id_hab = db.Column(db.Integer, nullable=False)
    data_res = db.Column(db.Date, nullable=False)
    id_hotel = db.Column(db.Integer, nullable=False)) 


    def __init__(self,num_res,id_hab,data_res,id_hotel): 
        self.num_res = num_res
        self.id_hab = id_hab
        self.data_res = data_res
        self.id_hotel = id_hotel


    @staticmethod
    def hab_res_read_all():
         # SELECT * from filmes ORDER BY id ASC
         all_habitacao = Habitacao.query.order_by(Habitacao.id_hab.asc()).all()
         output = []
         for habitacao in all_habitacao:   
             if (habitacao.id_hotel == 1):
                 salida = {}
                 salida['id_hab'] = habitacao.id_hab
                 salida['numero'] = habitacao.numero
                 salida['valor'] = habitacao.valor
                 salida['capacidade'] = habitacao.capacidade
                 salida['categoria'] = habitacao.categoria
                 salida['id_hotel'] =habitacao.id_hotel
                 salida['estado'] =habitacao.estado
                 output.append(salida)
         return output


    @staticmethod
    def habitacao_id_hotel(id_hotel):
        return Habitacao.query.get(id_hotel)


#-----------------------------------------------  Casse Habitacao -------------------------------------------------

class Habitacao(db.Model):
    __tablename__= "habitacao"
    id_hab = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Integer, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(255), nullable=False) 
    id_hotel = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)

    def __init__(self,numero,valor,capacidade,categoria,id_hotel,estado): 
        self.numero = numero
        self.valor = valor
        self.capacidade = capacidade
        self.categoria = categoria
        self.id_hotel = id_hotel
        self.estado = estado

    @staticmethod
    def habitacao_read_all():
         # SELECT * from filmes ORDER BY id ASC
         all_habitacao = Habitacao.query.order_by(Habitacao.id_hab.asc()).all()
         output = []
         for habitacao in all_habitacao:   
             if (habitacao.id_hotel == 1):
                 salida = {}
                 salida['id_hab'] = habitacao.id_hab
                 salida['numero'] = habitacao.numero
                 salida['valor'] = habitacao.valor
                 salida['capacidade'] = habitacao.capacidade
                 salida['categoria'] = habitacao.categoria
                 salida['id_hotel'] =habitacao.id_hotel
                 salida['estado'] =habitacao.estado
                 output.append(salida)
         return output


    @staticmethod
    def habitacao_id_hotel(id_hotel):
        return Habitacao.query.get(id_hotel)

#-----------------------------------------------  Casse Cliente -------------------------------------------------

class Clienteo(db.Model):
    __tablename__= "Cliente"
    id_cliente = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.Integer, nullable=False)
    sobrenomea = db.Column(db.String(255), nullable=False) 
    telefone = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)

    def __init__(self,numero,valor,capacidade,categoria,id_hotel,estado): 
        self.numero = numero
        self.valor = valor
        self.capacidade = capacidade
        self.categoria = categoria
        self.id_hotel = id_hotel
        self.estado = estado

    @staticmethod
    def habitacao_read_all():
         # SELECT * from filmes ORDER BY id ASC
         all_habitacao = Habitacao.query.order_by(Habitacao.id_hab.asc()).all()
         output = []
         for habitacao in all_habitacao:   
             if (habitacao.id_hotel == 1):
                 salida = {}
                 salida['id_hab'] = habitacao.id_hab
                 salida['numero'] = habitacao.numero
                 salida['valor'] = habitacao.valor
                 salida['capacidade'] = habitacao.capacidade
                 salida['categoria'] = habitacao.categoria
                 salida['id_hotel'] =habitacao.id_hotel
                 salida['estado'] =habitacao.estado
                 output.append(salida)
         return output


    @staticmethod
    def habitacao_id_hotel(id_hotel):
        return Habitacao.query.get(id_hotel)


#-----------------------------------------------  Casse Hotel -------------------------------------------------
#Modelar a Classe Hotel -> tabela hotel

class Hotel(db.Model):
    id_hotel = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    url_img = db.Column(db.String(255), nullable=False) 

    def __init__(self, nome, url_img):
        self.nome = nome
        self.url_img = url_img

    @staticmethod
    def read_all():
         # SELECT * from filmes ORDER BY id ASC
         return Hotel.query.order_by(Hotel.id_hotel.asc()).all()

    @staticmethod
    def read_id(registro_id):
        #SELECT * FROM filmes WHERE id=1
        return Hotel.query.get(registro_id)
        

@app.route('/')
def principal():
    tiempo=time.asctime()
    return render_template('index.html')

#----------------------------------------------- MENU DE RECEPÇÃO -----------------------------------------------------

@app.route("/menu_recep")
def menu_recep():
    return render_template("menu_recep.html")

@app.route("/menu_reserva")
def menu_reserva():
    return render_template("menu_reserva.html")

@app.route("/menu_clientes")
def menu_clientes():
    return render_template("menu_clientes.html")

@app.route("/menu_quartos", methods=['GET','POST'])
def menu_quartos():
    #return render_template("menu_quartos.html")
    #registros = Habitacao.habitacao_id_hotel(1)
    registros = Habitacao.habitacao_read_all()
    #Chama do método read_all da classe filmes, que representa a tabela filmes do banco de dados.
    return render_template("habitacao_read_all.html", registros=registros)

@app.route("/menu_faturacao")
def menu_faturacao():
    return render_template("menu_faturacao.html")
    
#-----------------------------------------------MENU DE RESERVAS  -----------------------------------------------------

@app.route("/menu_reserva/consultar_reserva")
def consultar_reserva():
        #return render_template("menu_quartos.html")
    #registros = Habitacao.habitacao_id_hotel(1)
    registros = Reserva.reserva_read_all()
    #Chama do método read_all da classe filmes, que representa a tabela filmes do banco de dados.
    return render_template("reserva_read_all.html", registros=registros)

@app.route("/menu_reserva/nova_reserva", methods=['GET','POST'])
def nova_reserva():
    novo_id = None
    novo_id2 = None
    novo_id3 = None
    if request.method == 'POST':
        form = request.form
        crear_reserva = Reserva(num_reserva=form['num_reserva'], data_in=form['data_in'], data_out=form['data_out'], id_cliente=form['id_cliente'])
        print(crear_reserva)
        db.session.add(crear_reserva)
        db.session.commit()

        novo_id = crear_reserva.num_reserva
        novo_id2 = crear_reserva.data_in
        novo_id3 = crear_reserva.data_out

    return render_template("nova_reserva.html", novo_id=novo_id, novo_id2=novo_id2, novo_id3=novo_id3)

@app.route("/menu_reserva/apagar_reserva/<numeroReserva>", methods=['GET','POST'])
def apagar_reserva(numeroReserva):
    if request.method == 'POST':
        reserva = Reserva.read_id(numeroReserva)
        Reserva.delete()
    return render_template("apagar_reserva.html")

@app.route("/menu_reserva/alterar_reserva/<numeroReserva>", methods=['GET','POST'])
def alterar_reserva(numeroReserva):
    if request.method == 'POST':
        form = request.form 
        reserva = Reserva.read_id(numeroReserva)
        Reserva.update( data_in= form['data_in'], data_out= form['data_out'])

    return render_template("alterar_reserva.html")

#-----------------------------------------------____________ -----------------------------------------------------

@app.route("/read")
def read_all():
    registros = Hotel.read_all()
    #Chama do método read_all da classe filmes, que representa a tabela filmes do banco de dados.
    return render_template("read_all.html", registros=registros)

@app.route("/read/<id_registro>")
def read_id(id_registro):
    registro = Hotel.read_id(id_registro)
    return render_template("read_all.html", registro=registro)

@app.route("/create")
def create():
    return "Em contrucao - Ainda sera feito o CREATE!"

if (__name__ == '__main__'):
    app.run(debug=True)

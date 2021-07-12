from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date


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
    __tablename__= "reserva"
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
    def reserva_read_all():
        # SELECT * from filmes ORDER BY id ASC
        all_reserva = Reserva.query.order_by(Reserva.data_in.asc()).all()
        output = []
        for reserva in all_reserva:   
            salida = {}
            salida['num_reserva'] = reserva.num_reserva
            salida['data_in'] = reserva.data_in
            salida['data_out'] = reserva.data_out
            salida['diferenca'] = abs((reserva.data_in - reserva.data_out).days)
            salida['id_cliente'] = reserva.id_cliente
            salida['nome'] = Cliente.query.get(reserva.id_cliente).nome
            output.append(salida)
        return output
    
    @staticmethod
    def reserva_id_cliente():
        # SELECT * from filmes ORDER BY id ASC
        all_reserva = Reserva.query.order_by(Reserva.data_in.asc()).all()
        output = []
        for reserva in all_reserva:   
            salida = {}
            salida['id_cliente'] = reserva.id_cliente
            output.append(salida)
        return output

    
    @staticmethod
    def consultar_reserva_single(numeroReserva):
            #print(numeroReserva)
            output = []
            reserva = Reserva.query.get(numeroReserva)
            #print(Reserva.query.get(numeroReserva))
            salida = {}
            salida['num_reserva'] = reserva.num_reserva
            salida['data_in'] = reserva.data_in
            salida['data_out'] = reserva.data_out
            salida['diferenca'] = abs((reserva.data_in - reserva.data_out).days)
            salida['id_cliente'] = reserva.id_cliente
            salida['nome'] = Cliente.query.get(reserva.id_cliente).nome
            salida['id_hab'] = Hab_res.consultar_hab(numeroReserva)
            salida['num_hab'] = Habitacao.habitacao_numero(salida['id_hab'])
            salida['categoria'] = Habitacao.habitacao_categoria(salida['id_hab'])
            salida['valor_u'] = Habitacao.habitacao_preco(salida['id_hab']).valor
            salida['valor_t'] = ((salida['valor_u'])*(salida['diferenca']))
            #salida ['id_hab'] = Hab_res.query.filter_by(numeroReserva=num_res).id_hab
            #salida['habitacao'] = 102
            output.append(salida)
            return salida

    @staticmethod
    def actualizar_reserva_single(numeroReserva):
            #print(numeroReserva)
            output = []
            reserva = Reserva.query.get(numeroReserva)
            #print(Reserva.query.get(numeroReserva))
            salida = {}
            salida['data_in'] = reserva.data_in
            salida['data_out'] = reserva.data_out
            output.append(salida)
            return output

    @staticmethod
    def reserva_read_single(id_registro):
        return Reserva.query.get(id_registro)
    
    def update(self, data_in, data_out):
        self.data_in = data_in
        self.data_out = data_out
        db.session.add(self) # adiciona o novo registro através da session ao DB
        db.session.commit()        
        #self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()        


#-----------------------------------------------  Casse Hab_Res -------------------------------------------------

class Hab_res(db.Model):
    __tablename__= "hab_res"
    num_res = db.Column(db.Integer, nullable=False)
    id_hab = db.Column(db.Integer, nullable=False)
    data_res = db.Column(db.Date, nullable=False)
    id_hotel = db.Column(db.Integer, nullable=False )
    id_num_res = db.Column(db.Integer, primary_key=True)


    def __init__(self,num_res,id_hab,data_res,id_hotel): 
        self.num_res = num_res
        self.id_hab = id_hab
        self.data_res = data_res
        self.id_hotel = id_hotel

    @staticmethod
    def consultar_hab(numeroReserva):
         all_habitacao = Hab_res.query.order_by(Hab_res.id_num_res.asc()).all()
         for habitacao in all_habitacao:  
            if (str(habitacao.num_res) == numeroReserva):
                return habitacao.id_hab

    @staticmethod
    def consultar_id(numeroReserva):
         all_habitacao = Hab_res.query.order_by(Hab_res.id_num_res.asc()).all()
         for habitacao in all_habitacao:  
            if (str(habitacao.num_res) == numeroReserva):
                return habitacao.id_num_res
    
    @staticmethod
    def hab_res_read_single(id_num_res):
        return Hab_res.query.get(id_num_res)

    def delete(self):
        db.session.delete(self)
        db.session.commit() 
   
        




#-----------------------------------------------  Clase Habitacao -------------------------------------------------

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

    @staticmethod
    def habitacao_numero(id_hab):
        return Habitacao.query.get(id_hab).numero

    @staticmethod
    def habitacao_categoria(id_hab):
        return Habitacao.query.get(id_hab).categoria

    @staticmethod
    def habitacao_preco(id_hab):
        return Habitacao.query.get(id_hab)

#-----------------------------------------------  Clase Cliente -------------------------------------------------

class Cliente(db.Model):
    __tablename__= "cliente"
    id_cliente = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.Integer)
    tipo = db.Column(db.String(255))
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False) 
    telefone = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(255))
    saldo = db.Column(db.Integer, nullable=False)
    id_hotel = db.Column(db.Integer, nullable=False)
    procedencia = db.Column(db.String(255))
    vip = db.Column(db.Boolean)

    def __init__(self,documento,tipo,nome,sobrenome,telefone,endereco, saldo, id_hotel, procedencia): 
        self.documento = documento
        self.tipo = tipo
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.endereco = endereco
        self.saldo = saldo
        self.id_hotel = id_hotel
        self.procedencia = procedencia


    @staticmethod
    def cliente_read_nome(id_cliente):
         # SELECT * from filmes ORDER BY id ASC
         all_nomes = Cliente.query.order_by(Cliente.id_cliente.asc()).all()
         output = []
         for nomes in all_nomes:  
             if (nomes.id_cliente == id_cliente): 
                 salida = {}
                 salida['nome'] = nomes.nome
                 output.append(salida)
         return output

    @staticmethod
    def cliente_all():
         # SELECT * from filmes ORDER BY id ASC
         all_cliente = Cliente.query.order_by(Cliente.id_cliente.asc()).all()
         output = []
         for cliente in all_cliente:  
                 salida = {}
                 salida['id_cliente'] = cliente.id_cliente
                 salida['documento'] = cliente.documento
                 salida['tipo'] = cliente.tipo
                 salida['nome'] = cliente.nome
                 salida['sobrenome'] = cliente.sobrenome
                 salida['telefone'] = cliente.telefone
                 salida['saldo'] = cliente.saldo
                 salida['id_hotel'] = cliente.id_hotel
                 salida['procedencia'] = cliente.procedencia
                 output.append(salida)
         return output


    @staticmethod
    def habitacao_id_hotel(id_hotel):
        return Habitacao.query.get(id_hotel)


#-----------------------------------------------  Clase Hotel -------------------------------------------------
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

@app.route("/menu_reserva/consultar_reserva", methods=['GET','POST'])
def consultar_reserva():
    registros = Reserva.reserva_read_all()
    return render_template("consultar_reserva.html", registros=registros)


@app.route("/menu_reserva/nova_reserva", methods=['GET','POST'])
def nova_reserva():
    novo_id = None
    novo_id2 = None
    novo_id3 = None
    if (request.method == 'POST'):
        form = request.form
        crear_reserva = Reserva(num_reserva=form['num_reserva'], data_in=form['data_in'], data_out=form['data_out'], id_cliente=form['id_cliente'])
        db.session.add(crear_reserva)
        db.session.commit()
        data_hoje = date.today()
        crear_res_hab = Hab_res(num_res= form['num_reserva'], id_hab=form['id_hab'] ,data_res= data_hoje, id_hotel=1)
        db.session.add(crear_res_hab)
        db.session.commit()
        novo_id = crear_reserva.num_reserva
        novo_id2 = crear_reserva.data_in
        novo_id3 = crear_reserva.data_out
    return render_template("nova_reserva.html", novo_id=novo_id, novo_id2=novo_id2, novo_id3=novo_id3)


@app.route("/menu_reserva/apagar_reserva/<numeroReserva>", methods=['GET','POST'])
def apagar_reserva(numeroReserva):
    apaga_reserva = Reserva.consultar_reserva_single(numeroReserva)

    id_hab_res = Hab_res.consultar_id(numeroReserva)

    apaga_hab_res = Hab_res.hab_res_read_single(id_hab_res)
    apaga_hab_res.delete()
    apaga_reserva = Reserva.reserva_read_single(numeroReserva)
    apaga_reserva.delete()
    return render_template("apagar_reserva.html")

@app.route("/menu_reserva/alterar_reserva/<numeroReserva>", methods=['GET','POST'])
def alterar_reserva(numeroReserva):
    registro = Reserva.consultar_reserva_single(numeroReserva)
    altera = Reserva.reserva_read_single(numeroReserva)
    if request.method == 'POST':
        form = request.form
        altera.update(data_in=form['data_in'], data_out=form['data_out'])
    return render_template("alterar_reserva.html", registro=registro, altera=altera)

@app.route('/menu_reserva/<num_reserva>', methods=['GET','POST'])
def ver_reserva(num_reserva):
    registro = Reserva.consultar_reserva_single(num_reserva)
    return render_template("ver_reserva.html", registro=registro)


#-----------------------------------------------MENU DE CLIENTES  -----------------------------------------------------

@app.route("/consultar_clientes", methods=['GET','POST'])
def listar_clientes():
    registros = Cliente.cliente_all()
    return render_template("consultar_clientes.html", registros=registros)

@app.route("/menu_reserva/novo_cliente", methods=['GET','POST'])
def novo_cliente():
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

    return render_template("novo_cliente.html", novo_id=novo_id, novo_id2=novo_id2, novo_id3=novo_id3)

@app.route("/menu_reserva/apagar_cliente/<numeroReserva>", methods=['GET','POST'])
def apagar_cliente(numeroReserva):
    if request.method == 'POST':
        reserva = Reserva.read_id(numeroReserva)
    return render_template("apagar_reserva.html")

@app.route("/menu_reserva/alterar_cliente/<numeroReserva>", methods=['GET','POST'])
def alterar_cliente(numeroReserva):
    if request.method == 'POST':
        form = request.form 
        reseva = Reserva.read_id(numeroReserva)
        reseva.update( data_in= form['data_in'], data_out= form['data_out'])


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

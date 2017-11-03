import os
import urlparse
import psycopg2

from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def homepage():   

	return render_template("index.html")


@app.route('/consultar', methods=['POST'])
def consultar():  

	codigo = request.form['tfcodigo']
	
	conn = psycopg2.connect("dbname=ddeqtbq831p5nl host=ec2-54-221-235-12.compute-1.amazonaws.com port=5432 user=omqkdsfcxcuukq password=13a0ed34cb33d12ad3be7c93ed10ed6e25c12fd213af2101b0c090f1c215d5d9 sslmode=require")

	sql = conn.cursor()

	sql.execute("SELECT * FROM estudiante WHERE codigo = %s;", [codigo])

	filas = sql.fetchall()

	conn.commit()

	sql.close()

	conn.close()
		
	return render_template("ResultadoConsulta.html", row = filas)


@app.route('/guardar', methods=['POST'])
def guardar():   
	
	nombre = request.form['tfnombre']
	codigo = request.form['tfcodigo']
	
	conn = psycopg2.connect("dbname=ddeqtbq831p5nl host=ec2-54-221-235-12.compute-1.amazonaws.com port=5432 user=omqkdsfcxcuukq password=13a0ed34cb33d12ad3be7c93ed10ed6e25c12fd213af2101b0c090f1c215d5d9 sslmode=require")

	sql = conn.cursor()

	sql.execute("INSERT INTO estudiante (codigo, nombre) VALUES (%s, %s)", [codigo, nombre])	

	estado = "" + nombre + " con codigo " + codigo + " se guardo con exito"

	conn.commit()

	sql.close()

	conn.close()

	return render_template("Guardar.html", status=estado)


@app.route('/buscar', methods=['GET','POST'])
def buscar():   

	return render_template("Consultar.html")


@app.route('/crear', methods=['GET','POST'])
def crear():   

	return render_template("Guardar.html")


def conexion():

	try:

		conn = psycopg2.connect("dbname=ddeqtbq831p5nl host=ec2-54-221-235-12.compute-1.amazonaws.com port=5432 user=omqkdsfcxcuukq password=13a0ed34cb33d12ad3be7c93ed10ed6e25c12fd213af2101b0c090f1c215d5d9 sslmode=require")

		return conn

	except:

		return """<h1>Lo siento, no se pudo establecer la conexion con la base de datos</h1>"""


def search(sql, param):

	try:

		return sql.execute(param)
		
	except:

		return """<h1>Se ha producido un error<h1>"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


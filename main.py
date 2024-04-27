# chat conversation
import json
import pymysql
import requests
import http.client
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")

    sql = '''
        update '''+DB_DDBB+'''.usuarios set
            nombre = "'''+str(request.json['nombre'])+'''",
            apellido = "'''+str(request.json['apellido'])+'''",
            telefono = "'''+str(request.json['telefono'])+'''",
            email = "'''+str(request.json['email'])+'''",
            contrasena = "'''+str(request.json['contrasena'])+'''",
            fecha_nacimiento = "'''+str(request.json['fecha_nacimiento'])+'''",
            genero = "'''+str(request.json['genero'])+'''",
            tipo_usuario = "'''+str(request.json['tipo_usuario'])+'''",
            status = "'''+str(request.json['status'])+'''",
            rut = "'''+str(request.json['rut'])+'''",
            carrera = "'''+str(request.json['carrera'])+'''",
            anoIngresoCarrera = "'''+str(request.json['anoIngresoCarrera'])+'''",
            jornada = "'''+str(request.json['jornada'])+'''",
            direccion = "'''+str(request.json['direccion'])+'''",
            region = "'''+str(request.json['region'])+'''",
            comuna = "'''+str(request.json['comuna'])+'''",
            entrevistador = "'''+str(request.json['entrevistador'])+'''",
        WHERE id = %s;
    '''
    cursor.execute(sql, request.json['id'])
    connection.commit()
    return retorno

    #except Exception as e:
    #    print('Error: '+ str(e))
    #    retorno = {           
    #        "detalle":"algo falló", 
    #        "validacion":False
    #    }
    #    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')
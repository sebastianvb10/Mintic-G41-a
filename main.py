from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from controladores.ControladorCandidato import ControladorCandidato
from controladores.ControladorMesa import ControladorMesa
from controladores.ControladorPartido import ControladorPartido
from controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)
#creacion de constructores
controlMesa= ControladorMesa()
controlCandi= ControladorCandidato()
controlPartido= ControladorPartido()
controlResultado= ControladorResultado()

#--------------------------------------------------------------------------------------------------------------
#metodos de Mesa
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#creacion de mesa
#--------------------------------------------------------------------------------------------------------------
@app.route("/mesa", methods=['POST'])
def crearMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlMesa.crearMesa(requestBody)
    if result:
        return {"resultado": "Mesa Creado!"}
    else:
        return {"resultado": "Error al crear la Mesa!"}
#--------------------------------------------------------------------------------------------------------------
#metodos de obtencion de datos
#--------------------------------------------------------------------------------------------------------------
@app.route("/mesa", methods=['GET'])
def GETMesa():
    result = controlMesa.buscartodasMesas()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
@app.route("/mesa/<string:idObject>", methods=['GET'])
def GETMesas(idObject):
    result = controlMesa.buscarMesa(idObject)
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
#metodo de actualizacion
#--------------------------------------------------------------------------------------------------------------
@app.route("/mesa", methods=['PUT'])
def PutMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlMesa.actualizarMesa(requestBody)
    if result:
        return {"resultado": "Mesa actualizado"}
    else:
        return {"resultado": "Error al actualizar el Mesa"}
#--------------------------------------------------------------------------------------------------------------
#metodo borrar
#--------------------------------------------------------------------------------------------------------------
@app.route("/mesa", methods=['DELETE'])
def DeleteMesa(idObject):
    controlMesa.eliminarMesa(idObject)
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#metodos de Candidato
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#creacion de mesa
#--------------------------------------------------------------------------------------------------------------
@app.route("/candidato", methods=['POST'])
def crearCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlCandi.crearCandidato(requestBody)
    if result:
        return {"resultado": "Candidato Creado!"}
    else:
        return {"resultado": "Error al crear el Candidato!"}
#--------------------------------------------------------------------------------------------------------------
#metodos de obtencion de datos
#--------------------------------------------------------------------------------------------------------------
@app.route("/candidato", methods=['GET'])
def GETtodosCandidato():
    result = controlCandi.buscarTodosLosCandidatos()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
@app.route("/candidato/<string:idObject>", methods=['GET'])
def GETCandidato(idObject):
    result = controlCandi.buscarCandidato(idObject)
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
#metodo de actualizacion
#--------------------------------------------------------------------------------------------------------------
@app.route("/candidato", methods=['PUT'])
def PutCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlCandi.actualizarCandidato(requestBody)
    if result:
        return {"resultado": "Candidato actualizado"}
    else:
        return {"resultado": "Error al actualizar el Candidato"}
#--------------------------------------------------------------------------------------------------------------
#metodo borrar
#--------------------------------------------------------------------------------------------------------------
@app.route("/candidato/<string:idObject>", methods=['DELETE'])
def DeleteCandidato(idObject):
    controlCandi.eliminarCandidato(idObject)
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#metodos de Partido
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#creacion de Partido
#--------------------------------------------------------------------------------------------------------------

@app.route("/partido", methods=['POST'])
def crearPartido():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlPartido.crearPartido(requestBody)
    if result:
        return {"resultado": "Partido Creado!"}
    else:
        return {"resultado": "Error al crear el Partido!"}
#--------------------------------------------------------------------------------------------------------------
#Obtencion de datos
#--------------------------------------------------------------------------------------------------------------
@app.route("/partido", methods=['GET'])
def GETPartido():
    result = controlPartido.buscartodosPartido()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
@app.route("/partido/<string:idObject>", methods=['GET'])
def GETPartidos(idObject):
    result = controlCandi.buscarCandidato(idObject)
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
@app.route("/partido", methods=['PUT'])
def PutPartido():
    controlPartido.actualizarPartido()
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/partido", methods=['DELETE'])
def DeletePartido():
    controlPartido.eliminarPartido()
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


@app.route("/resultado", methods=['POST'])
def crearResultado():
    controlResultado.crearResultado()
    return {"resultado": "Crea Resultado"}


@app.route("/resultado", methods=['GET'])
def GETResultado():
    controlResultado.buscarResultado()
    variableRespuesta = {
        "respuesta": "GET realizada"
    }
    return variableRespuesta


@app.route("/resultado", methods=['PUT'])
def PutResultado():
    controlResultado.actualizarResultado()
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/resultado", methods=['DELETE'])
def DeleteResultado():
    controlResultado.eliminarResultado()
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

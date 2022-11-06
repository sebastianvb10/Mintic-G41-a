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
#metodo de asignacion partido
#--------------------------------------------------------------------------------------------------------------
@app.route("/candidato/<string:idCandidato>/partido/<string:idPartido>", methods=['PUT'])
def AsignarPartidoCandidato(idCandidato,idPartido):
    result = controlCandi.asignarPartido(idCandidato,idPartido)
    return jsonify(result)#convierte a json
#-------------------------------------------------------------------
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

@app.route("/partido/candidato/<string:idCandidato>/mea/<string:idMesa>", methods=['POST'])
def crearPartido(idCandidato,idMesa):
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlPartido.crearPartido(requestBody,idCandidato,idMesa)
    if result:
        return jsonify(result)
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
def GETtodosPartidos(idObject):
    result = controlPartido.buscarPartido(idObject)
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
#metodo de actualizacion
#--------------------------------------------------------------------------------------------------------------
@app.route("/partido", methods=['PUT'])
def PutPartido():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlPartido.actualizarPartido(requestBody)
    if result:
        return {"resultado": "Paritod actualizado"}
    else:
        return {"resultado": "Error al actualizar el Partido"}
#--------------------------------------------------------------------------------------------------------------
#metodo borrar
#--------------------------------------------------------------------------------------------------------------
@app.route("/partido", methods=['DELETE'])
def DeletePartido(idObject):
    controlPartido.eliminarPartido(idObject)
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#metodos de Resultado
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#creacion de Resultado
#--------------------------------------------------------------------------------------------------------------


@app.route("/resultado", methods=['POST'])
def crearResultado():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlResultado.crearResultado(requestBody)
    if result:
        return {"resultado": "Resultado Creado!"}
    else:
        return {"resultado": "Error al crear el Resultado!"}
#--------------------------------------------------------------------------------------------------------------
#Obtencion de datos
#--------------------------------------------------------------------------------------------------------------
@app.route("/resultado", methods=['GET'])
def GETResultado():
    result = controlResultado.buscarTodosResultado()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
@app.route("/partido/<string:idObject>", methods=['GET'])
def GETPartidos(idObject):
    result = controlResultado.buscarResultado(idObject)
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)
#--------------------------------------------------------------------------------------------------------------
#metodo de actualizacion
#--------------------------------------------------------------------------------------------------------------
@app.route("/resultado", methods=['PUT'])
def PutResultado():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlResultado.actualizarResultado(requestBody)
    if result:
        return {"resultado": "Resultado actualizado"}
    else:
        return {"resultado": "Error al actualizar el Resultado"}
#--------------------------------------------------------------------------------------------------------------
#metodo borrar
#--------------------------------------------------------------------------------------------------------------

@app.route("/resultado", methods=['DELETE'])
def DeleteResultado(idObject):
    controlResultado.eliminarResultado(idObject)
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

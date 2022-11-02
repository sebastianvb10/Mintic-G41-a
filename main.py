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
controladorMesa= ControladorMesa()
controlCandi= ControladorCandidato()
controladorPartido= ControladorPartido()
controladorResultado= ControladorResultado()


@app.route("/mesa", methods=['POST'])
def crearMesa():
    controladorMesa.crearMesa()
    return {"resultado": "Crea mesa"}


@app.route("/mesa", methods=['GET'])
def GETMesa():
    controladorMesa.buscarMesa()
    variableRespuesta = {
        "respuesta": "GET realizada"
    }
    return variableRespuesta


@app.route("/mesa", methods=['PUT'])
def PutMesa():
    controladorMesa.actualizarMesa()
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/mesa", methods=['DELETE'])
def DeleteMesa():
    controladorMesa.eliminarMesa()
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


@app.route("/candidato", methods=['POST'])
def crearCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controlCandi.crearCandidato(requestBody)
    if result:
        return {"resultado": "Candidato Creado!"}
    else:
        return {"resultado": "Error al crear el Candidato!"}


@app.route("/candidato", methods=['GET'])
def GETCandidato():
    result = ControladorCandidato.buscarTodosLosCandidatos()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato", methods=['PUT'])
def PutCandidato():
    ControladorCandidato.actualizarCandidato()
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/candidato", methods=['DELETE'])
def DeleteCandidato():
    ControladorCandidato.eliminarCandidato()
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


@app.route("/partido", methods=['POST'])
def crearPartido():
    controladorPartido.crearPartido()
    return {"resultado": "Crea Partido"}


@app.route("/partido", methods=['GET'])
def GETPartido():
    controladorPartido.buscarPartido()
    variableRespuesta = {
        "respuesta": "GET realizada"
    }
    return variableRespuesta


@app.route("/partido", methods=['PUT'])
def PutPartido():
    controladorPartido.actualizarPartido()
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/partido", methods=['DELETE'])
def DeletePartido():
    controladorPartido.eliminarPartido()
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


@app.route("/resultado", methods=['POST'])
def crearResultado():
    controladorResultado.crearResultado()
    return {"resultado": "Crea Resultado"}


@app.route("/resultado", methods=['GET'])
def GETResultado():
    controladorResultado.buscarResultado()
    variableRespuesta = {
        "respuesta": "GET realizada"
    }
    return variableRespuesta


@app.route("/resultado", methods=['PUT'])
def PutResultado():
    controladorResultado.actualizarResultado()
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/resultado", methods=['DELETE'])
def DeleteResultado():
    controladorResultado.eliminarResultado()
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

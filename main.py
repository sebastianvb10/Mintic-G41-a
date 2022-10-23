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
controladorMesa: ControladorMesa()
controladorCandidato: ControladorCandidato()
controladorPartido: ControladorPartido()
controladorResultado: ControladorResultado()


@app.route("/mesa", methods=['POST'])
def crearMesa():
    controladorMesa.crearMesa()
    return {"resultado": "Crea mesa"}


@app.route("/mesa", methods=['COPY'])
def CopyMesa():
    controladorMesa.buscarMesa()
    variableRespuesta = {
        "respuesta": "copy realizada"
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
    controladorCandidato.crearCandidato()
    return {"resultado": "Crea Candidato"}


@app.route("/candidato", methods=['COPY'])
def CopyCandidato():
    controladorCandidato.buscarCandidato()
    variableRespuesta = {
        "respuesta": "copy realizada"
    }
    return variableRespuesta


@app.route("/candidato", methods=['PUT'])
def PutCandidato():
    controladorCandidato.actualizarCandidato()
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/candidato", methods=['DELETE'])
def DeleteCandidato():
    controladorCandidato.eliminarCandidato()
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


@app.route("/partido", methods=['POST'])
def crearPartido():
    controladorPartido.crearPartido()
    return {"resultado": "Crea Partido"}


@app.route("/partido", methods=['COPY'])
def CopyPartido():
    controladorPartido.buscarPartido()
    variableRespuesta = {
        "respuesta": "copy realizada"
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


@app.route("/resultado", methods=['COPY'])
def CopyResultado():
    controladorResultado.buscarResultado()
    variableRespuesta = {
        "respuesta": "copy realizada"
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

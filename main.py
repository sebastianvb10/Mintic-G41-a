from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)



@app.route("/mesa",methods=['POST'])

def crearMesa():

        return {"resultado": "Crea mesa"}


    
@app.route("/mesa",methods=['COPY'])

def CopyMesa():
    variableRespuesta={
        "respuesta":"copy realizada"
    }
    return variableRespuesta

@app.route("/mesa",methods=['PUT'])

def PutMesa():
    variableRespuesta={
        "respuesta":"PUT realizado"
    }
    return variableRespuesta
@app.route("/mesa",methods=['DELETE'])

def DeleteMesa():
    variableRespuesta={
        "respuesta":"DELETE realizado"
    }
    return variableRespuesta


@app.route("/candidato", methods=['POST'])
def crearCandidato():
    return {"resultado": "Crea Candidato"}


@app.route("/candidato", methods=['COPY'])
def CopyCandidato():
    variableRespuesta = {
        "respuesta": "copy realizada"
    }
    return variableRespuesta


@app.route("/candidato", methods=['PUT'])
def PutCandidato():
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/candidato", methods=['DELETE'])
def DeleteCandidato():
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


@app.route("/partido", methods=['POST'])
def crearPartido():
    return {"resultado": "Crea Partido"}


@app.route("/partido", methods=['COPY'])
def CopyPartido():
    variableRespuesta = {
        "respuesta": "copy realizada"
    }
    return variableRespuesta


@app.route("/partido", methods=['PUT'])
def PutPartido():
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/partido", methods=['DELETE'])
def DeletePartido():
    variableRespuesta = {
        "respuesta": "DELETE realizado"
    }
    return variableRespuesta


@app.route("/resultado", methods=['POST'])
def crearResultado():
    return {"resultado": "Crea Resultado"}


@app.route("/resultado", methods=['COPY'])
def CopyResultado():
    variableRespuesta = {
        "respuesta": "copy realizada"
    }
    return variableRespuesta


@app.route("/resultado", methods=['PUT'])
def PutResultado():
    variableRespuesta = {
        "respuesta": "PUT realizado"
    }
    return variableRespuesta


@app.route("/resultado", methods=['DELETE'])
def DeleteResultado():
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

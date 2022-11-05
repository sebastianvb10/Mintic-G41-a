from Repositorios.RepositorioResultado import RepositorioResultado
from modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Entro al constructor de la clase  ControladorResultado")
        self.repositorioResultado = RepositorioResultado()
    def crearResultado(self, bodyR):
        print("Creando el Resultado....")
        nuevoResultado = Resultado(bodyR)
        print("Resultado a crear en base de datos: ", nuevoResultado.__dict__)
        self.repositorioResultado.save(nuevoResultado)
        return True
    def buscarResultado(self, idObject):
        print("Buscando el Resultado....", idObject)
        resultado = Resultado(self.repositorioResultado.findById(idObject))
        return resultado.__dict__
    def buscarTodosResultado(self):
        print("Buscando todos los Resultados en base de datos....")
        return self.repositorioResultado.findAll()
    def eliminarResultado(self, idObject):
        print("Eliminando el Resultado....", idObject)
        self.repositorioResultado.delete(idObject)
        return True
    def actualizarResultado(self, result):
        resultActual = Resultado(self.repositorioResultado.findById(result["idObject"]))
        print("Actualizando el Candidato....", resultActual.__dict__)
        resultActual.id = result["id"]
        resultActual.numeroMesa = result["numeroMesa"]
        resultActual.cedulaCandidato = result["cedulaCandidato"]
        resultActual.numeroVotos = result["numeroVotos"]
        self.repositorioResultado.save(resultActual)
        return True
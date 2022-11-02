

from modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorCandidato():

    def __init__(self):
        print("Entró al constructor de la clase ControladorCandidato")
        self.repositorioCandidato = RepositorioCandidato()

    def crearCandidato(self, bodyR):
        print("Creando el Candidato....")
        nuevoCandidato = Candidato(bodyR)
        print("Candidato a crear en base de datos: ", nuevoCandidato.__dict__)
        self.repositorioCandidato.save(nuevoCandidato)
        return True

    def buscarCandidato(self, idObject):
        print("Buscando el Candidato....", idObject)
        candidato = Candidato(self.repositorioCandidato.findById(idObject))
        return Candidato.__dict__

    def buscarTodosLosCandidatos(self):
        print("Buscando todos los Candidatos en base de datos....")
        return self.repositorioCandidato.findAll()

    def actualizarCandidato(self, Candidato):
        CandidatoActual = Candidato(self.repositorioCandidato.findById(Candidato["idObject"]))
        print("Actualizando el Candidato....", CandidatoActual)
        CandidatoActual.nombre = Candidato["nombre"]
        CandidatoActual.apellido = Candidato["apellido"]
        CandidatoActual.cedula = Candidato["cedula"]
        self.repositorioCandidato.save(CandidatoActual)
        return True

    def eliminarCandidato(self, idObject):
        print("Eliminando el Candidato....", idObject)
        self.repositorioCandidato.delete(idObject)
        return True
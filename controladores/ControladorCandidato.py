from Repositorios.RepositorioPartido import RepositorioPartido
from modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato
from modelos.Partido import Partido


class ControladorCandidato():

    def __init__(self):
        print("Entró al constructor de la clase ControladorCandidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def crearCandidato(self, bodyR):
        print("Creando el Candidato....")
        nuevoCandidato = Candidato(bodyR)
        print("Candidato a crear en base de datos: ", nuevoCandidato.__dict__)
        self.repositorioCandidato.save(nuevoCandidato)
        return True

    def buscarCandidato(self, idObject):
        print("Buscando el Candidato....", idObject)
        candidato = Candidato(self.repositorioCandidato.findById(idObject))
        return candidato.__dict__

    def buscarTodosLosCandidatos(self):
        print("Buscando todos los Candidatos en base de datos....")
        return self.repositorioCandidato.findAll()

    def actualizarCandidato(self, candi):
        candiActual = Candidato(self.repositorioCandidato.findById(candi["idObject"]))
        print("Actualizando el Candidato....", candiActual.__dict__)
        candiActual.nombre = candi["nombre"]
        candiActual.apellido = candi["apellido"]
        candiActual.cedula = candi["cedula"]
        candiActual.numeroResolucion = candi["numeroResolucion"]
        self.repositorioCandidato.save(candiActual)
        return True

    def eliminarCandidato(self, idObject):
        print("Eliminando el Candidato....", idObject)
        self.repositorioCandidato.delete(idObject)
        return True
    def asignarPartido(self,idCandidato,idPartido):
        candi=Candidato(self.repositorioCandidato.findById(idCandidato))
        parti=Partido(self.repositorioPartido.findById((idPartido)))
        candi.IdPartido=parti
        self.repositorioCandidato.save(candi)
        return candi

from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioResultado import RepositorioResultado
from modelos.Candidato import Candidato
from modelos.Mesa import Mesa
from modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Entro al constructor de la clase  ControladorResultado")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato= RepositorioCandidato()
        self.repositorioMesa=RepositorioMesa()
    def crearResultado(self, bodyR,idCandidato,idMesa):
        print("Creando el Resultado....")
        nuevoResultado = Resultado(bodyR)
        candi=Candidato(self.repositorioCandidato.findById(idCandidato))
        mes=Mesa(self.repositorioMesa.findById(idMesa))
        nuevoResultado.candidato=candi
        nuevoResultado.mesa=mes
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

        return self.repositorioResultado.save(resultActual)
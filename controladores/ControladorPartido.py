from Repositorios.RepositorioPartido import RepositorioPartido
from modelos.Partido import Partido


class ControladorPartido():
    def __init__(self):
        print("Entro al constructor de la clase  ControladorPartido")
        self.repositorioPartido = RepositorioPartido()
    def crearPartido(self,bodyR):
        print("Creando el Partido....")
        nuevoPartido = Partido(bodyR)
        print("Partido a crear en base de datos: ", nuevoPartido.__dict__)
        self.repositorioPartido.save(nuevoPartido)
        return True
    def buscarPartido(self,idObject):
        print("Buscando el Partido....", idObject)
        partido = Partido(self.repositorioPartido.findById(idObject))
        return partido.__dict__
    def buscartodosPartido(self):
        print("Buscando todos los Partidos en base de datos....")
        return self.repositorioPartido.findAll()
    def eliminarPartido(self,idObject):
        print("Eliminando el Partido....", idObject)
        self.repositorioPartido.delete(idObject)
        return True
    def actualizarPartido(self,partidorecibido):
        partidoActual = Partido(self.repositorioPartido.findById(partidorecibido["idObject"]))
        print("Actualizando el Partido....", partidoActual.__dict__)
        partidoActual.id = partidorecibido["id"]
        partidoActual.nombre = partidorecibido["nombre"]
        partidoActual.lema = partidorecibido["lema"]
        self.repositorioPartido.save(partidoActual)
        return True
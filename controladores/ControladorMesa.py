from Repositorios.RepositorioMesa import RepositorioMesa
from modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        print("Entro al constructor de la clase  ControladorMesa")
        self.repositorioMesa = RepositorioMesa()

    def crearMesa(self, bodyR):
        print("Creando el Mesa....")
        nuevaMesa = Mesa(bodyR)
        print("Mesa a crear en base de datos: ", nuevaMesa.__dict__)
        self.repositorioMesa.save(nuevaMesa)
        return True

    def buscarMesa(self, idObject):
        print("Buscando el Candidato....", idObject)
        mesa = Mesa(self.repositorioMesa.findById(idObject))
        return mesa.__dict__

    def buscartodasMesas(self):
        print("Buscando todos las Mesas en base de datos....")
        return self.repositorioMesa.findAll()

    def eliminarMesa(self,idObject):
        print("Eliminando el Mesa....", idObject)
        self.repositorioMesa.delete(idObject)
        return True

    def actualizarMesa(self, mesarecibida):
        mesaActual = Mesa(self.repositorioMesa.findById(mesarecibida["idObject"]))
        print("Actualizando el Mesa....", mesaActual.__dict__)
        mesaActual.numero = mesarecibida["numero"]
        mesaActual.cantidadInscritos = mesarecibida["cantidadInscritos"]
        self.repositorioMesa.save(mesaActual)
        return True
from trabajo import Trabajo
from repositorioTrabajos import RepositorioTrabajos


class ListaTrabajos:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.lista = self.rt.get_all()

    def nuevo_trabajo(
        self,
        cliente,
        fecha_entrega_propuesta,
        descripcion,
        fecha_ingreso,
    ):
        t = Trabajo(
            cliente,
            fecha_entrega_propuesta,
            descripcion,
            fecha_ingreso,
        )
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.lista.append(t)
            return t

#! /usr/bin/env python3
from repositorioTrabajos import RepositorioTrabajos


class Informe:
    def __init__(self):
        self.rt = RepositorioTrabajos()

    def imprimir_informe(self, id_cliente):
        trabajos = self.rt.get_by_client_id(id_cliente)
        for trabajo in trabajos:
            print("==============================")
            print(trabajo)
            print("==============================")

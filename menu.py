#! /usr/bin/env python3
import sys
import datetime
from listaClientes import ListaClientes
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from listaTrabajos import ListaTrabajos
from informe import Informe


class Menu:
    """Mostrar un menú y responder a las opciones"""

    def __init__(self):
        self.rc = RepositorioClientes()
        self.rt = RepositorioTrabajos()
        self.opciones = {
            "0": self.salir,
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.eliminar_cliente,
            "4": self.modificar_cliente,
            "5": self.nuevo_trabajo,
            "6": self.mostrar_trabajos,
            "7": self.modificar_trabajo,
            "8": self.marcar_finalizado,
            "9": self.marcar_entregado,
            "10": self.eliminar_trabajo,
            "11": self.imprimir_informe
        }

    def mostrar_menu(self):
        print(
            """
Menú del sistema:
0. Salir
1. Mostrar todos los clientes 
2. Ingresar los datos de un nuevo cliente
3. Eliminar cliente
4. Modificar cliente
5. Cargar trabajo nuevo
6. Mostrar todos los trabajos 
7. Modificar trabajo
8. Marcar trabajo como finalizado
9. Marcar trabajo como entregado
10. Eliminar trabajo
11. Imprimir informe de trabajos por cliente
"""
        )

    def ejecutar(self):
        """Mostrar el menu y responder a las opciones."""
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_clientes(self, lista=None):
        if lista == None:
            lista = ListaClientes().lista
        for Cliente in lista:
            print(Cliente)
            print("==============================")

    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C:Corporativo / P:Particular")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
            contacto = input("Ingrese el nombre del contacto: ")
            tc = input("Ingrese el telefono del contacto: ")
        else:
            apellido = input("Ingrese el apellido: ")
        tel = input("Ingrese el telefono: ")
        mail = input("Ingrese el correo electronico: ")
        if tipo in ("C", "c"):
            c = ListaClientes().nuevo_cliente_corporativo(
                nombre, contacto, tc, tel, mail
            )
        else:
            c = ListaClientes().nuevo_cliente_particular(
                nombre, apellido, tel, mail
            )

        if c is None:
            print("Error al cargar el cliente")
        else:
            print("Cliente cargado correctamente")

    def eliminar_cliente(self):
        id_cliente = input("Ingrese el ID del cliente: ")
        cliente = self.rc.get_one(id_cliente)
        if cliente is None:
            print("No existe el cliente")

        else:
            cliente_eliminado = self.rc.delete(cliente)
            if cliente_eliminado is True:
                print("El cliente se elimino correctamente")
            else:
                print("No se pudo eliminar")

    def modificar_cliente(self):
        id_cliente = input("Ingrese el ID del cliente: ")
        cliente = self.rc.get_one(id_cliente)
        if cliente is None:
            print("No existe el cliente")
        else:
            print(cliente)
            nuevo_nombre = input("Ingrese el nombre: ")
            cliente.nombre = nuevo_nombre
            if type(cliente).__name__ == "ClienteCorporativo":
                nuevo_contacto = input("Ingrese el nombre del contacto: ")
                cliente.nombre_contacto = nuevo_contacto
                nuevo_tc = input("Ingrese el telefono del contacto: ")
                cliente.telefono_contacto = nuevo_tc
            else:
                nuevo_apellido = input("Ingrese el apellido: ")
                cliente.apellido = nuevo_apellido
                nuevo_tel = input("Ingrese el telefono: ")
                cliente.telefono = nuevo_tel
                nuevo_mail = input("Ingrese el correo electronico: ")
                cliente.mail = nuevo_mail

            cliente_modificado = self.rc.update(cliente)
            if cliente_modificado is True:
                print("El cliente se modifico correctamente")
            else:
                print("No se pudo modificar")

    def nuevo_trabajo(self):
        id_cliente = input("Ingrese el ID del cliente: ")
        cliente = self.rc.get_one(id_cliente)
        if cliente is None:
            print("No existe el cliente")

        else:
            date_entry = input("Ingrese una fecha de ingreso con formato YYYY-MM-DD: ")
            year, month, day = map(int, date_entry.split("-"))
            fecha_ingreso = datetime.date(year, month, day)

            date_entry = input(
                "Ingrese una fecha de entrega propuesta con formato YYYY-MM-DD: "
            )
            year, month, day = map(int, date_entry.split("-"))
            fecha_entrega_propuesta = datetime.date(year, month, day)

            descripcion = input("Ingrese una descripcion para el trabajo: ")
            t = ListaTrabajos().nuevo_trabajo(
                cliente, fecha_entrega_propuesta, descripcion, fecha_ingreso
            )

            if t is None:
                print("Error al cargar el trabajo")
            else:
                print("Trabajo cargado correctamente")

    def mostrar_trabajos(self, lista=None):
        if lista == None:
            lista = ListaTrabajos().lista
        for Trabajos in lista:
            print(Trabajos)
            print("==============================")

    def modificar_trabajo(self):
        id_trabajo = input("Ingrese el ID del trabajo: ")
        trabajo = self.rt.get_one(id_trabajo)
        if trabajo is None:
            print("No existe el trabajo")
        else:
            print(trabajo)
            date_entry = input("Ingrese una nueva fecha de ingreso con formato YYYY-MM-DD: ")
            year, month, day = map(int, date_entry.split("-"))
            fecha_ingreso = datetime.date(year, month, day)

            date_entry = input(
                "Ingrese una nueva fecha de entrega propuesta con formato YYYY-MM-DD: "
            )
            year, month, day = map(int, date_entry.split("-"))
            fecha_entrega_propuesta = datetime.date(year, month, day)

            descripcion = input("Ingrese una nueva descripcion para el trabajo: ")

            trabajo.fecha_ingreso = fecha_ingreso
            trabajo.fecha_entrega_propuesta = fecha_entrega_propuesta
            trabajo.descripcion = descripcion

            finalizado = "A"
            while finalizado not in ("S", "s", "N", "n"):
                finalizado = input("¿Fue finalizado? (S)í / (N)o: ")
            if finalizado in ("S", "s"):
                date_entry = input("Ingrese la fecha de finalización con formato YYYY-MM-DD: ")
                year, month, day = map(int, date_entry.split("-"))
                fecha_entrega = datetime.date(year, month, day)
                trabajo.fecha_entrega_real = fecha_entrega
            else:
                trabajo.fecha_entrega_real = None

            entregado = "A"
            while entregado not in ("S", "s", "N", "n"):
                entregado = input("¿Fue entregado? (S)í / (N)o: ")
            if entregado in ("S", "s"):
                trabajo.retirado = True
            else:
                trabajo.retirado = False

            trabajo_modificado = self.rt.update(trabajo)
            if trabajo_modificado is True:
                print("El trabajo se modifico correctamente")
            else:
                print("No se pudo modificar")

    def marcar_finalizado(self):
        id_trabajo = input("Ingrese el ID del trabajo: ")
        trabajo = self.rt.get_one(id_trabajo)
        if trabajo is None:
            print("No existe el trabajo")
        else:
            trabajo.fecha_entrega_real = datetime.date.today()
            trabajo_modificado = self.rt.update(trabajo)
            if trabajo_modificado is True:
                print("El trabajo se modifico correctamente")
                print("==============================")
                print(trabajo)
            else:
                print("No se pudo modificar")

    def marcar_entregado(self):
        id_trabajo = input("Ingrese el ID del trabajo: ")
        trabajo = self.rt.get_one(id_trabajo)
        if trabajo is None:
            print("No existe el trabajo")
        else:
            trabajo.retirado = True
            trabajo_modificado = self.rt.update(trabajo)
            if trabajo_modificado is True:
                print("El trabajo se modifico correctamente")
                print("==============================")
                print(trabajo)
            else:
                print("No se pudo modificar")

    def eliminar_trabajo(self):
        id_trabajo = input("Ingrese el ID del trabajo: ")
        trabajo = self.rt.get_one(id_trabajo)
        if trabajo is None:
            print("No existe el trabajo")
        else:
            trabajo_eliminado = self.rt.delete(trabajo)
            if trabajo_eliminado is True:
                print("El trabajo se elimino correctamente")
            else:
                print("No se pudo eliminar")

    def imprimir_informe(self):
        id_cliente = input("Ingrese el ID del cliente: ")
        cliente = self.rc.get_one(id_cliente)
        if cliente is None:
            print("No existe el cliente")
        else:
            Informe().imprimir_informe(id_cliente)

    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().ejecutar()

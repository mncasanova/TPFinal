#! /usr/bin/env python3
import sys
import datetime
from listaClientes import ListaClientes
from repositorioClientes import RepositorioClientes
from listaTrabajos import ListaTrabajos


class Menu:
    """Mostrar un menú y responder a las opciones"""

    def __init__(self):
        self.rc = RepositorioClientes()
        self.lista_clientes = ListaClientes()
        self.lista_trabajos = ListaTrabajos()
        self.opciones = {
            "0": self.salir,
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.eliminar_cliente,
            "4": self.modificar_cliente,
            "5": self.nuevo_trabajo,
            "6": self.mostrar_trabajos,
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
            lista = self.lista_clientes.lista
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
            c = self.lista_clientes.nuevo_cliente_corporativo(
                nombre, contacto, tc, tel, mail
            )
        else:
            c = self.lista_clientes.nuevo_cliente_particular(
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
            t = self.lista_trabajos.nuevo_trabajo(
                cliente, fecha_entrega_propuesta, descripcion, fecha_ingreso
            )

            if t is None:
                print("Error al cargar el trabajo")
            else:
                print("Trabajo cargado correctamente")

    def mostrar_trabajos(self, lista=None):
        if lista == None:
            lista = self.lista_trabajos.lista
        for Trabajos in lista:
            print(Trabajos)
            print("==============================")

    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().ejecutar()

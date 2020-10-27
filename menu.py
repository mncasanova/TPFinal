#! /usr/bin/env python3
import sys
from listaClientes import ListaClientes
class Menu:
    '''Mostrar un menú y responder a las opciones'''
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.opciones= {
            "0": self.salir,
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            
        }

    def mostrar_menu(self):
        print("""
Menú del sistema:
0. Salir
1. Mostrar todos los clientes 
2. Ingresar los datos de un nuevo cliente
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))
                
    def mostrar_clientes(self, lista = None):
        if lista == None:
           lista = self.lista_clientes.lista
        for Cliente in lista:
            print(Cliente)
            print("==============================")

    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C","c","P","p"):
          tipo = input("Ingrese el tipo de cliente: C:Corporativo / P:Particular")
        nombre = input ("Ingrese el nombre: ")
        if tipo in ("C", "c"):
          contacto =input("Ingrese el nombre del contacto: ")
          tc = input("Ingrese el telefono del contacto: ")
        else: 
            apellido =input ("Ingrese el apellido: ")
        tel = input ("Ingrese el telefono: ")
        mail = input("Ingrese el correo electronico: ")
        if tipo in ("C", "c"):
           c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
           c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)

        if c is None:
            print("Error al cargar el cliente")
        else:
            print("Cliente cargado correctamente")


    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().ejecutar()

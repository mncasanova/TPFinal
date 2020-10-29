#! /usr/bin/python3

import datetime


class Trabajo:
    """Representa un trabajo de reparación que realizará el taller"""

    def __init__(
        self,
        cliente,
        fecha_entrega_propuesta,
        descripcion,
        fecha_ingreso=datetime.date.today(),
        fecha_entrega_real=None,
        retirado=False,
        id_trabajo=None,
    ):
        """Recibe un objeto cliente, una fecha de ingreso (objeto datetime),
        otros dos objetos datetime con la fecha de entrega propuesta y real,
        una descripción, un valor "retirado" (True o False) y un id opcional"""
        self.cliente = cliente
        self.fecha_ingreso = fecha_ingreso
        self.fecha_entrega_propuesta = fecha_entrega_propuesta
        self.fecha_entrega_real = fecha_entrega_real
        self.descripcion = descripcion
        self.retirado = retirado
        self.id_trabajo = id_trabajo

    def __str__(self):
        cadena = (
            f"ID Trabajo: {self.id_trabajo} - ID Cliente: {self.cliente.id_cliente}\n"
        )
        cadena += f"Fecha ingreso: {self.fecha_ingreso} - Fecha propuesta: {self.fecha_entrega_propuesta}\n"
        cadena += f"Descripcion: {self.descripcion}\n"
        cadena += f"Fecha entrega real: {self.fecha_entrega_real}\n"
        cadena += f"Retirado: {self.retirado}\n"
        return cadena

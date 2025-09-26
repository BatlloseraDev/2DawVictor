import random as r
import numpy as np

from persona import Persona

class Heroe(Persona):



    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador, **kwargs):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.__codigoLimpio = kwargs.get("codigoLimpio",generarValorAleatorio())
        self.__bienDocumentado= kwargs.get("bienDocumentado",generarValorAleatorio())
        self.__gitgod= kwargs.get("gitgod",generarValorAleatorio())
        self.__arquitecto= kwargs.get("arquitecto",generarValorAleatorio())
        self.__detallista = kwargs.get("detallista",generarValorAleatorio())


    def get_puntuacion(self):

        contador = round(self.__codigoLimpio * 0.4 + self.__bienDocumentado * 0.1 + self.__gitgod * 0.2 + self.__arquitecto * 0.2 + self.__detallista * 0.1)
        self.__puntuacion_total = contador
        return self.__puntuacion_total


def generarValorAleatorio():
    return r.randint(1, 100)
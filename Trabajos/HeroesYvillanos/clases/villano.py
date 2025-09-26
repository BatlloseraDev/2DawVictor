
import random as r
from persona import Persona

class Villano(Persona):


    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador, **kwargs):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.__chagepeteador= kwargs.get("chagepeteador",generarValorAleatorio())
        self.__entregadorTardio= kwargs.get("entregadorTardio",generarValorAleatorio())
        self.__ausencias = kwargs.get("ausencias",generarValorAleatorio())
        self.__hablador = kwargs.get("hablador",generarValorAleatorio())



def generarValorAleatorio():
    return r.randint(1, 100)
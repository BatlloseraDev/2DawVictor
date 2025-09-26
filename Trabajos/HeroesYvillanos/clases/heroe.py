import random as r
import numpy as np

from clases.persona import Persona

class Heroe(Persona):



    def __init__(self, nombre, apellidos, fecha_nacimiento, **kwargs):
        super().__init__(nombre, apellidos, fecha_nacimiento)
        self.__codigoLimpio = kwargs.get("codigoLimpio",generarValorAleatorio())
        self.__bienDocumentado= kwargs.get("bienDocumentado",generarValorAleatorio())
        self.__gitgod= kwargs.get("gitgod",generarValorAleatorio())
        self.__arquitecto= kwargs.get("arquitecto",generarValorAleatorio())
        self.__detallista = kwargs.get("detallista",generarValorAleatorio())
        self.__calcular_puntuacion()

    def __calcular_puntuacion(self):
        contador = round(
            self.__codigoLimpio * 0.4 + self.__bienDocumentado * 0.1 + self.__gitgod * 0.2 + self.__arquitecto * 0.2 + self.__detallista * 0.1)
        self.__puntuacion_total = contador

    #getter and setter
    #estos parametros solo van a ser de get ya que lo calculo en la clase
    @property
    def codigoLimpio(self):
        return self.codigoLimpio


    @property
    def bienDocumentado(self):
        return self.bienDocumentado




def generarValorAleatorio():
    return r.randint(1, 100)
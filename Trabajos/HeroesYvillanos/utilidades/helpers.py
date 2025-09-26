from modelos.heroe import Heroe
from modelos.villano import Villano


class Helper:

    rutaGuardadoHeroe= "data/heroes.txt"
    rutaGuardadoVillano = "data/villanos.txt"

    @staticmethod
    def convertirObjetoATexto(objeto):
        texto = ""
        if type(objeto) is Heroe :
            texto +="Heroe/"
            arrais= vars(objeto)
            for key, value in arrais.items():
                texto += f"{key}:{value}/"

        elif type(objeto) is Villano :
            texto += "Vilano/"
            arrais = vars(objeto)
            for key, value in arrais.items():
                texto += f"{value}/"

        else:
            return False, "error al convertir un objeto a texto"
        return True, texto

    @staticmethod
    def convertirTextoAObjeto():
        pass

    @staticmethod
    def devolverRutaGuardado(tipo):
        if tipo == 1:
            return Helper.rutaGuardadoHeroe
        elif tipo == 2:
            return Helper.rutaGuardadoVillano
        else:
            return None
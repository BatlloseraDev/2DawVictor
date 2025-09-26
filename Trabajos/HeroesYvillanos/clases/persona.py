class Persona:
    contador = 0
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        Persona.contador += 1
        self.__identificador = Persona.contador
        self.__puntuacion_total = 0

    @property #solo get ya que set va a ser calculado por la propia clase al momento de crearse.
    def puntuacion_total(self):
        return self.__puntuacion_total

    #getters and setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value

    @property
    def fecha_nac(self):
        return self.__fecha_nac

    @fecha_nac.setter
    def fecha_nac(self, value):
        self.__fecha_nac = value

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, value):
        self.__identificador = value


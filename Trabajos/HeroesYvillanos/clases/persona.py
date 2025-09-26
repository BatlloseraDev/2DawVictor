class Persona:

    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        self.__identificador = identificador
        self.__puntuacion_total = 0

    def get_puntuacion(self):
        return self.__puntuacion_total

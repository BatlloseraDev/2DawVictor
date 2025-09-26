from numpy.f2py.auxfuncs import throw_error

from clases.heroe import Heroe
from clases.villano import Villano
from datetime import datetime
from log import Logger




def controladorTeclado(texto, tipoDato):
    texto = texto.strip() #controlo los espacios
    if tipoDato == "entero":
        try:
            dato= int(texto)
            return dato
        except ValueError:
            return None

    elif tipoDato == "texto":
        if texto == "":
            return None
        else:
            return texto
    else:
        return None



def menu():
    print("1) Para crear Heroe")
    print("2) Para crear Villano")
    print("3) Para buscar un heroe o villano")
    print("4) Para salir")

def gestionAulaDeHeroesYVillanos(opcion):
    valores = {}
    valores['nombre'] = controladorTeclado(input("Ingrese el nombre: "), "texto")
    valores['apellidos'] = controladorTeclado(input("Ingrese los apellidos: "), "texto")

    dia_nacimiento = controladorTeclado(input("Ingrese el dia nacimiento: "), "entero")
    mes_nacimiento = controladorTeclado(input("Ingrese el mes nacimiento: "), "entero")
    anio_nacimiento = controladorTeclado(input("Ingrese el anio nacimiento: "), "entero")

    try:
        fecha_nacimiento = datetime(anio_nacimiento, mes_nacimiento, dia_nacimiento)
        valores['fecha_nacimiento'] = fecha_nacimiento
    except:
        return False, "la fecha no es valida"

    if None in valores:
        return False, "algún campo no fue introducido correctamente"

    if opcion == 1:
        return True,"héroe creado" ,Heroe(valores["nombre"], valores["apellidos"], valores["fecha_nacimiento"])
    elif opcion == 2:
        return True,"villano creado" ,Villano(valores["nombre"], valores["apellidos"], valores["fecha_nacimiento"])
    else:
        return False, "el desarrollador introdujo una opción no valida para probar"


def main():
    listaPersonas = []
    log = Logger()

    try:
        while True:
            menu()
            opcion = int(input("Que eliges"))

            if opcion == 3:
                print("buscando..")
            elif opcion == 4:
                break
            elif opcion >= 5 or opcion <= 0:
                print("Selecciona una opcion valida")
            else:
                resultado = gestionAulaDeHeroesYVillanos(opcion)
                if resultado[0]:
                    listaPersonas.append(resultado[2])
                    log.log("INFO",resultado[2])

                else:
                    throw_error(listaPersonas[1])


    except Exception as e:
        log.log("ERROR", e)


if __name__ == "__main__":
    main()






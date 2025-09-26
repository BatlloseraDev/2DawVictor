

#from numpy.f2py.auxfuncs import throw_error

from modelos.heroe import Heroe
from modelos.villano import Villano
from datetime import datetime

from utilidades.fileManager import FileManager
from utilidades.helpers import Helper
from utilidades.logger import Logger




def controladorTeclado(texto, tipoDato): #Para controlar los datos que pido por teclado
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
    print("4) Para enfrentar un heroe contra un villano")
    print("5) Para salir")



def gestionAulaDeHeroesYVillanos(opcion):
    valores = {
        'nombre': controladorTeclado(input("Ingrese el nombre: "), "texto"),
        'apellidos': controladorTeclado(input("Ingrese los apellidos: "), "texto")}

    dia_nacimiento = controladorTeclado(input("Ingrese el dia nacimiento: "), "entero")
    mes_nacimiento = controladorTeclado(input("Ingrese el mes nacimiento: "), "entero")
    anio_nacimiento = controladorTeclado(input("Ingrese el anio nacimiento: "), "entero")

    if None in [dia_nacimiento, mes_nacimiento, anio_nacimiento]:
        print("Fallo aquí")
        return False, f"Algun campo de la fecha no fue valido, será representado con None: d{dia_nacimiento}, m{mes_nacimiento}, y{anio_nacimiento}"
    else:
        try:
            fecha_nacimiento = datetime(anio_nacimiento, mes_nacimiento, dia_nacimiento)
            valores['fecha_nacimiento'] = fecha_nacimiento
        except Exception as e:
            return False, f"la fecha no es valida: {e}"

    if None in valores.values():
        return False, f"algún campo no fue introducido correctamente en nombres{valores["nombre"]} o apellidos{valores["apellidos"]} "

    if opcion == 1:
        heroe = Heroe(valores["nombre"], valores["apellidos"], valores["fecha_nacimiento"])
        return True,"héroe creado" ,heroe
    elif opcion == 2:
        # guardar en data
        return True,"villano creado" ,Villano(valores["nombre"], valores["apellidos"], valores["fecha_nacimiento"])
    else:
        return False, "el desarrollador introdujo una opción no valida para probar"



def main():
    listaPersonas = []
    log = Logger()
    log.log("INFO","Iniciado el sistema")
    try:
        while True:
            menu()
            opcion = int(input("Que eliges\n"))

            if opcion == 3:
                print("buscando..")
            elif opcion == 5:
                log.log("INFO","El usuario finalizó la sesión")
                break
            elif opcion >= 6 or opcion <= 0:
                print("Opción invalida")
                log.log("ALERT",f"El usuario es especial y no introdujo correctamete la opción: {opcion}")
            else:
                log.log("INFO","Iniciado el proceso de creación de Héroe o Villano")
                resultado = gestionAulaDeHeroesYVillanos(opcion)
                if resultado[0]:
                    listaPersonas.append(resultado[2])
                    log.log("INFO",resultado[2])
                    guardado= Helper.convertirObjetoATexto(resultado[2])
                    if guardado[0]:
                        FileManager.guardar(Helper.devolverRutaGuardado(opcion),guardado[1])
                    else:
                        log.log("Error",f"error al guardar en la base de datos: {guardado[1]}")

                else:
                    print(f"Error en la creación de personaje, volviendo al menú: {resultado[1]}")
                    log.log("ERROR",f"Hubo un error creando el personaje: {resultado[1]}")


    except Exception as e:
        log.log("ERROR", f"{e}") # {traceback.format_exc()} para devolver la ultima linea del error
        log.log("INFO","Cerrando el sistema automaticamente")
    except KeyboardInterrupt:
        log.log("INFO", "El usuario cerró el programa abruptamente")


if __name__ == "__main__":
    main()






'''En esta clase hacer toda la gestion del log'''
from datetime import datetime
import os




class Logger:
    def __init__(self): #no me gustaba que el dia se eligiese en la creacion del objeto en vez de en la creacion del mensaje
                        #ya que si se empieza una sesion a las 23:59:00 y ocurre un accion a las 00:01:15 esta se escribiría en el dia anterior
        self.nombre_fichero= f"log/ErrorCreandoFichero_HEROESYVILLANOS.log"


    def log(self,tipo,mensaje):
        self.generarFichero()

        timestamp = datetime.now().strftime("%d%m%Y %H:%M:%S")
        linea_log = f"[{timestamp}] ---- [{tipo}] ---- {mensaje}\n"

        with open(self.nombre_fichero, 'a',encoding='utf-8') as file: #tuve que buscar como escribir en un fichero y encontré lo del encoding
            file.write(linea_log)
            print(f"Guardado en log:{linea_log}")

    def generarFichero(self):
        fecha = datetime.now().strftime("%Y%m%d").lower()#de esta manera se ordenan automaticamente los log
        self.nombre_fichero= f"log/{fecha}_HEROESYVILLANOS.log"
        os.makedirs(os.path.dirname(self.nombre_fichero) if os.path.dirname(self.nombre_fichero) else '.', exist_ok=True) #para crear los directorios padre necesarios en caso de resultarlos




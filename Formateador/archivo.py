import csv
import json
import os

class Archivo:
    def __init__(self, nombreUsuario:str, ruta:str):
        self._nombreUsuario = nombreUsuario
        self._ruta = ruta
    
    """
    Se valida la existencia y correcto formato en CSV del archivo que se encuentra en la ruta recibida.
    Retorna: falso si no cumple con los criterios.
    """
    def validarExistencia(self):
        if os.path.exists(self._ruta) and os.path.isfile(self._ruta) and self._ruta.endswith('.csv'):
            return True
        else:
            return False
        
    """
    Se valida que el archivo CSV recibido tenga 3 columnas.
    Recibe: el delimitador del archivo CSV.
    Retorna: falso si no cumple con los criterios.
    """
    def validarFormato(self, delimitador):
        if self.validarExistencia():
            with open(self._ruta, 'r', newline='') as archivo_csv:
                lectorCsv = csv.reader(archivo_csv, delimiter=delimitador)
                for fila in lectorCsv:
                    if len(fila) != 3:
                        print("El archivo CSV debe tener 3 columnas, formato incorrecto") 
                        return False
                return True
        else:
            print('El archivo indicado no existe, o no se encuentra en formato .csv')
        

archivo = Archivo('Miguel Cardona', 'C:/datos/archivos/estudiantes.csv')
archivo.validarFormato(';')



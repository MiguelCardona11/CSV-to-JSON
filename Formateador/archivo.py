import csv
import json
import os
import unidecode

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
        
    """
    Crea un archivo JSON en la misma ruta que el archivo CSV usando el mismo nombre, si el archivo ya existe, lo reemplaza.
    """
    def crearArchivoJson(self):
        carpeta = os.path.dirname(self._ruta)
        nombre = os.path.splitext(os.path.basename(self._ruta))[0]
        rutaJson = carpeta+'/'+nombre+'.json'
        
        nombreArchivo = rutaJson
        isFile = os.path.isfile(nombreArchivo)

        if (not isFile):
            with open(nombreArchivo, 'w') as fp:
                pass
        else:
            os.remove(rutaJson)
            with open(nombreArchivo, 'w') as fp:
                pass
        return rutaJson
    
    """
    Después de validar los datos del archivo CSV, se llena un nuevo archivo JSON con estos datos en su nuevo formato
    """
    def formatearJson(self):
        if self.validarFormato(';'):
            archivoJson = self.crearArchivoJson()
            archivoCsv = self._ruta
            
            diccionarioJson = {}
            with open(archivoCsv) as archivoCsv:
                datosCsv = csv.DictReader(archivoCsv)
                diccionarioJson["estudiantes"]=[]
                
                for fila_datos in datosCsv:
                    fila_limpia = {k: unidecode.unidecode(v) for k, v in fila_datos.items()}
                    diccionarioJson["estudiantes"].append(fila_limpia)
            
            with open(archivoJson, 'w') as archivoJson:
                archivoJson.write(json.dumps(diccionarioJson, indent=4))


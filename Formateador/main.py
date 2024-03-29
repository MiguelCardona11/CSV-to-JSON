from archivo import Archivo

def main():
    fin = False

    while not fin:
        try:
            nombreUsuario = input("Ingrese su nombre completo: ")
            ruta = input("Ingrese la ruta completa del archivo CSV: ")

            archivo = Archivo(nombreUsuario, ruta)
            archivo.formatearJson()
            fin = True
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()


import json
from Prestamo import *
from Socio import *
from Libro import *
import os
import pathlib
from datetime import datetime

# Valores de Menu de Prestamos
class Prestamos:
    SALIR = 0
    REGISTRAR_PRESTAMO = 1
    REGISTRAR_DEVOLUCION = 2
    REPORTE_DE_PRESTAMOS = 3

    def __init__(self, libros, socios):                         # Constructor donde se crea lista de prestamos
        self._prestamos = []
        self.ultimo_id = 0
        self.libros_obj = libros
        self.socios_obj = socios
        self.recuperar_prestamos('prestamos.json')              # Recuperar prestamos de ruta para que se agreguen a la lista de recuperar_prestamos

    def __del__(self):                                          # Destructor de clase
        self.guardar_prestamos ('prestamos.json')

    @property
    def ultimo_id(self):
        return self._ultimo_id
    @ultimo_id.setter
    def ultimo_id(self, valor):
        self._ultimo_id = valor
    @ultimo_id.deleter
    def ultimo_id(self):
        del self._ultimo_id

    @property
    def prestamos (self):
        return self._prestamos
    @prestamos.setter
    def prestamos (self,valor):
        self._prestamos = valor
    @prestamos.deleter
    def prestamos (self):
        del self._prestamos

    @property
    def libros_obj (self):
        return self._libros
    @libros_obj.setter
    def libros_obj (self,valor):
        self._libros = valor
    @libros_obj.deleter
    def libros_obj (self):
        del self._libros

    @property
    def socios_obj (self):
        return self._socios
    @socios_obj.setter
    def socios_obj (self,valor):
        self._socios = valor
    @socios_obj.deleter
    def socios_obj (self):
        del self._socios

    def recuperar_prestamos(self, ruta):
        if pathlib.Path(ruta).exists():
            with open(ruta, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            self._ultimo_id = datos.get('ultimo_id', 0)
            for prestamo in datos['prestamos']:
                self._prestamos.append(traer_desde_json_Prestamo(prestamo))

    def guardar_prestamos(self, ruta):
        # Que se abra el archivo como escritura (por eso la 'w')
        with open (ruta, 'w',encoding='utf-8') as archivo:
             # Escribir esa informacion usando la clase creada en Libro (se usa indent para que sea mas legible a la anidacion con 4 espacios)
            json.dump({'ultimo_id': self._ultimo_id, 'prestamos':self.prestamos}, archivo, cls=prestamo_Encoder, indent=4)

    def obtener_libro_por_id(self, id_libro):
        for libro in self.libros_obj.libros:
            if libro.id == id_libro:
                return libro
        return None
    
    def obtener_socio_por_id(self, id_socio):
        for socio in self.socios_obj.socios:
            if socio.id == id_socio:
                return socio
        return None
    
    def obtener_prestamo(self, id_prestamo):
        for prestamo in self._prestamos:
            if prestamo.id_prestamo == id_prestamo:
                return prestamo
        return None
    
    def imprimir_prestados(self):
        print(f"{str('ID').center(10)} | {str('Libro').center(30)} | {str('Socio').center(30)} | {str('F. Préstamo').center(15)} |")
        print('-' * 96)
        for prestamo in self.prestamos:
            if prestamo.estado_prestamo == 'Prestado':
                libro = self.obtener_libro_por_id(prestamo.id_libro)
                socio = self.obtener_socio_por_id(prestamo.id_socio)
                nombre_libro = libro.titulo if libro else "Desconocido"
                nombre_socio = f"{socio.nombre} {socio.apellido}" if socio else "Desconocido"
                print(f"{str(prestamo.id_prestamo).center(10)} | {str(nombre_libro).center(30)} | {str(nombre_socio).center(30)} | {str(prestamo.fecha_prestamo).center(15)} |")
        print("")
  
    def registrar_prestamo(self):                                # Registrar prestamo
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                             Registrar Préstamos')
            self.socios_obj.imprimir_socios()
            print("  Presione '0' para volver al menú anterior\n")
            id_socio = input("ID del socio: ")

            if id_socio.strip() == '':  # Si el valor está vacío, mostrar mensaje y pedir de nuevo
                print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
                input("Presione enter para continuar.")
                continue  # Volver a solicitar el ID
            
            if id_socio == '0':
                input("Volviendo al menu. Presione Enter para continuar.")
                break

            socio = self.obtener_socio_por_id(id_socio)
            if not socio:
                input("Socio no encontrado. Presione enter para continuar.")
                continue

            while True:    
                os.system('cls' if os.name == 'nt' else 'clear')
                print('             Registrar Préstamo')
                self.libros_obj.imprimir_libros()
                print("  Presione '0' para volver al menú anterior\n")

                id_libro = input("ID del libro: ")

                if id_libro.strip() == '':  # Si el valor está vacío, mostrar mensaje y pedir de nuevo
                    print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
                    input("Presione enter para continuar.")
                    continue  # Volver a solicitar el ID

                if id_libro == '0':
                    input("Volviendo al menu. Presione Enter para continuar.")
                    return

                libro = self.obtener_libro_por_id(id_libro)

                if not libro:
                    input("Libro no encontrado. Presione enter para continuar.")
                    continue
                
                if libro:
                # Verificar si el libro ya está prestado al socio
                    libro_prestado = False
                    for prestamo in self._prestamos:
                        if (prestamo.id_socio == id_socio and prestamo.id_libro == id_libro and prestamo.estado_prestamo == "Prestado"):
                            input(f"El libro ya ha sido prestado al socio {socio.nombre} {socio.apellido}. Presione enter para continuar.")
                            #si alguna de estas condiciones se cumple quiere decir que esta prestado y es True
                            libro_prestado = True
                            break

                    if libro_prestado:
                        break

                    if libro.cantidad_disp == "0":
                        input("No hay libros en stock. Presione enter para continuar")
                        break  # Volver a solicitar el ID del libro
                    else:
                        self._ultimo_id += 1
                        fecha_prestamo = datetime.now().strftime("%d-%m-%Y")
                        prestamo = Prestamo(str(self._ultimo_id), id_socio, id_libro, fecha_prestamo, None, "Prestado")
                        self._prestamos.append(prestamo)
                        libro.cantidad_disp = str(int(libro.cantidad_disp) - 1)
                        self.libros_obj.guardar_libros('libros.json')
                        self.guardar_prestamos('prestamos.json')
                        print(f"Préstamo registrado con éxito. ID de préstamo: {self._ultimo_id}")
                        input("Presione enter para continuar.")
                        break
                continue

    def registrar_devolucion(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                     Registrar Devolución')
            self.imprimir_prestados()
            print("  Presione '0' para volver al menú anterior\n")

            if not any(prestamo.estado_prestamo == 'Prestado' for prestamo in self.prestamos):
                os.system('cls' if os.name == 'nt' else 'clear')
                print('                    Consultar Libros')
                print("No hay prestamos en curso")
                input("Presione enter para continuar.")
                return

            id_prestamo = input("ID del préstamo: ")
            prestamo = self.obtener_prestamo(id_prestamo)
            
            if id_prestamo == '0':
                input("Volviendo al menu. Presione Enter para continuar.")
                break

            prestamo = self.obtener_prestamo(id_prestamo)

            if not prestamo or prestamo.estado_prestamo != 'Prestado':
                print("Préstamo no encontrado.")
                input("Presione enter para continuar.")
                continue

            prestamo.estado_prestamo = "Devuelto"
            prestamo.fecha_devolucion = datetime.now().strftime("%d-%m-%Y")
            libro = self.obtener_libro_por_id (prestamo.id_libro)
            libro.cantidad_disp = str(int(libro.cantidad_disp) + 1)
            self.libros_obj.guardar_libros('libros.json')
            self.guardar_prestamos('prestamos.json')
            print("Devolución registrada con éxito.")
            input("Presione enter para continuar.")

    def reporte_prestamos(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(str("Reporte de prestamos").center(120))
        print ("")
        if not self._prestamos:
            print("No hay préstamos registrados.")
        else:
            print(f"{str('ID').center(10)} | {str('Libro').center(30)} | {str('Socio').center(30)} | {str('F. Préstamo').center(15)} | {str('F. Devolución').center(15)} | {str('Estado').center(10)} |")
            print('-' * 127)
            for prestamo in self._prestamos:
                if prestamo.fecha_devolucion is not None:
                    fecha_devolucion = prestamo.fecha_devolucion
                else:
                    fecha_devolucion = "-"

                libro = self.obtener_libro_por_id(prestamo.id_libro)
                socio = self.obtener_socio_por_id(prestamo.id_socio)
                nombre_libro = libro.titulo if libro else "Desconocido"
                nombre_socio = f"{socio.nombre} {socio.apellido}" if socio else "Desconocido"

                print(f"{str(prestamo.id_prestamo).center(10)} | {str(nombre_libro).center(30)} | {str(nombre_socio).center(30)} | {str(prestamo.fecha_prestamo).center(15)} | {str(fecha_devolucion).center(15)} | {str(prestamo.estado_prestamo).center(10)} |")
        print ("")
        input("Presione enter para continuar.")

    def menu(self):                     # MENU DE PRESTAMOS
        continuar = True
        while continuar:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''             Biblioteca - Préstamos
                   {Prestamos.REGISTRAR_PRESTAMO}) Registrar Préstamo
                   {Prestamos.REGISTRAR_DEVOLUCION}) Registrar Devolución
                   {Prestamos.REPORTE_DE_PRESTAMOS}) Reporte de Préstamos
                   {Prestamos.SALIR}) Salir ''')
            opc = input("Selecciona una Opción: ")
            try:
                opc = int(opc)
            except ValueError:
                opc = -1
            match opc:
                case Prestamos.REGISTRAR_PRESTAMO:
                    self.registrar_prestamo()
                case Prestamos.REGISTRAR_DEVOLUCION:
                    self.registrar_devolucion()
                case Prestamos.REPORTE_DE_PRESTAMOS:
                    self.reporte_prestamos()
                case Prestamos.SALIR:
                    continuar = False
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Opción no Válida.')
                    input("Presione enter para continuar.")

                
# id prestamo
# id_socio extraer de lista de socios
# id_ libro extraer de id de libros y restar libros en stock
# agregar fecha de prestamo

# Registrar Devolucion
# id_prestamo
# id_socio extraer de lista de socios
# id_ libro extraer de id de libros y sumar libros en stock
# agregar fecha de devolucion

# Reporte de prestamos
    # "id_prestamo": 1,
    # "id_socio": 1,
    # "id_libro": 1,
    # "fecha_prestamo": "2024-02-01",
    # "fecha_devolucion": "2024-02-15",
    # "estado_prestamo": "Devuelto"
    


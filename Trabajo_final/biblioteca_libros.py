import json
from Libro import *
import os
import pathlib

# Valores de Menu de libros
class Libros:
    SALIR = 0
    REGISTRAR_LIBRO = 1
    CONSULTAR_LIBRO = 2
    ELIMINAR_LIBRO = 4
    EDITAR_LIBRO = 3

    # Constructor donde se crea coleccion de libros
    def __init__(self):
        self._libros = []
        self.ultimo_id = 0
        # Recuperar libros de ruta para que se agreguen a la lista de recuperar_libros
        self.recuperar_libros('libros.json')

    # Destructor de clase
    def __del__(self):
        self.guardar_libros ('libros.json')

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
    def libros (self):
        return self._libros
    @libros.setter
    def libros (self,valor):
        self._libros = valor
    @libros.deleter
    def libros (self):
        del self._libros

        # VALIDAR QUE NO HAYA CAMPOS VACÍOS
    def _validar_input(self, nombre_campo):
        valor = input(f"{nombre_campo}: ")
        while not valor.strip():  # Verifica si el valor está vacío
            print(f"El {nombre_campo.lower()} no puede estar vacío. Favor ingrese un {nombre_campo.lower()} válido.")
            valor = input(f"{nombre_campo}: ")
        return valor

        # RECUPERAR LIBROS DESDE JSON
    def recuperar_libros (self, ruta):
        # Si existe la ruta
        if pathlib.Path (ruta).exists():
            # Que se abra el archivo como lectura (por eso la 'r')
            with open (ruta, 'r',encoding='utf-8') as archivo:
                datos = json.load(archivo)
            # Recuperar ultimo_id
            self._ultimo_id = datos.get('ultimo_id', 0)
            # A partir del diccionario crea el libro y lo regresa
            for libro in datos ['libros']:
                self.libros.append(traer_desde_json_Libro(libro))

    def guardar_libros (self,ruta):
        # Que se abra el archivo como escritura (por eso la 'w')
        with open (ruta, 'w',encoding='utf-8') as archivo:
            # Escribir esa informacion usando la clase creada en Libro (se usa indent para que sea mas legible a la anidacion con 4 espacios)
            json.dump({'ultimo_id': self._ultimo_id, 'libros':self.libros}, archivo, cls=libro_Encoder, indent=4)

    def imprimir_libros(self):      # Para imprimir lista de libros
            print(f"  {'ID':<5} | {'Titulo':^25} | {'Autor':^30} | {'Editorial':^20} | {'Año':^8} | {'Género':^10} | {'Disponibles':^10}")
            print('-' * 130)
            for lib in self.libros:
                print(f"  {lib.id:<5} | {lib.titulo:^25} | {lib.autor:^30} | {lib.editorial:^20} | {lib.anio:^8} | {lib.genero:^10} | {lib.cantidad_disp:^10}")
            print("")

    def agregar_libros (self):
        # Limpiar consola
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('                    Agregar Libro')
        titulo = self._validar_input("Título")
        autor = self._validar_input("Autor")
        editorial = self._validar_input("Editorial")
        anio = self._validar_input("Año")
        genero = self._validar_input("Género")
        cant_disp = self._validar_input(("Cantidad Disponible"))

         # Incrementar el último ID y agregar el nuevo libro
        self._ultimo_id += 1
        self.libros.append (Libro(str(self._ultimo_id),titulo,autor,editorial,anio,genero,cant_disp))
        self.guardar_libros('libros.json')


    def consultar_libros (self):
        if len(self.libros) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                    Consultar Libros')
            print("No hay Libros registrados")
            input("Presione enter para continuar.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                    Consultar Libros')
            self.imprimir_libros()
            input ("Presione Enter para continuar.")

    def eliminar_libros(self):
        def limpiar_consola():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                     Eliminar Libro')
            print("Libros disponibles para eliminar:")
            self.imprimir_libros()

        while True:
            if len(self.libros) == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('                    Consultar Libros')
                print("No hay Libros registrados")
                input("Presione enter para continuar.")
                break

            limpiar_consola()
            print("  Presione '0' para volver al menú anterior\n")
            id_libro = input("Ingrese el ID del libro que desea eliminar: ")
               
            if id_libro == '0':
                print("Operación cancelada. Presione Enter para continuar.")
                input()
                break           
                
            if id_libro.strip() == '':  # Si el valor está vacío, mostrar mensaje y pedir de nuevo
                print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
                input("Presione enter para continuar.")
                limpiar_consola()
                print("  Presione '0' para volver al menú anterior\n")
                continue  # Volver a solicitar el ID

            encontrado = False

            for libro in self.libros:
                if libro.id == id_libro:
                    encontrado = True
                    limpiar_consola()
                    print(f"¿Desea eliminar el libro '{libro.titulo}'?")
                    print("     0. Cancelar")
                    print("     1. Confirmar")
                    confirmacion = input("Ingrese el número de la opción que desea realizar: ")

                    if confirmacion == '1':
                        self.libros.remove(libro)
                        self.guardar_libros('libros.json')  # Guardar cambios en el archivo JSON
                        limpiar_consola ()
                        print(f"Libro '{libro.titulo}' eliminado exitosamente. Presione Enter para continuar.")
                        input ()
                    elif confirmacion == '0':
                        print("Operación cancelada. Presione Enter para continuar.")
                    else:
                        print("Opción no válida. Operación cancelada. Presione Enter para continuar.")
                    break
            
            if not encontrado:
                limpiar_consola()
                print("  Presione '0' para volver al menú anterior\n")
                print(f"No se encontró ningún libro con ID '{id_libro}'. Presione Enter para continuar.")
                input()


    def editar_libros(self):      
        def limpiar_consola():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                     Editar Libros')
            print("Libros disponibles para editar:")
            self.imprimir_libros()

        while True:
            if len(self.libros) == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('                     Editar Libro')
                print("No hay Libros registrados")
                input("Presione enter para continuar.")
                break

            limpiar_consola()
            print("  Presione '0' para volver al menú anterior\n")
            id_libro = input("Ingrese el ID del Libro que desea editar: ")
            
            if id_libro.strip() == '':  # Si el valor está vacío, mostrar mensaje y pedir de nuevo
                print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
                input("Presione enter para continuar.")
                continue  # Volver a solicitar el ID

            if id_libro == '0':
                print("Volviendo al menu. Presione Enter para continuar.")
                input()
                break

            encontrado = False

            for libro in self.libros:
                if libro.id == id_libro:
                    encontrado = True
                    limpiar_consola()
                    print(f"¿Desea editar el libro '{libro.nombre}'?")
                    print("     0. Cancelar")
                    print("     1. Confirmar")
                    confirmacion = input("Ingrese el número de la opción que desea realizar: ")
                    limpiar_consola()
                    
                    if confirmacion == '1':
                        nombre = input("Nombre: ")
                        autor = input("Autor: ")
                        editorial = input("Editorial: ")
                        anio = input("Año: ")
                        genero = input("Género: ")
                        disp = input("Disponibilidad: ")

                            # Actualizar los datos del libro
                        if nombre.strip():
                            libro.nombre = nombre
                        if autor.strip():
                            libro.apellido = autor
                        if editorial.strip():
                            libro.f_nacim = editorial
                        if anio.strip():
                            libro.direccion = anio
                        if genero.strip():
                            libro.correo = genero
                        if disp.strip():
                            libro.telefono = disp

                        self.guardar_libros('libros.json')  # Guardar los cambios en el archivo JSON
                        limpiar_consola ()
                        print("Libro actualizado correctamente.")
                        input("Presione enter para continuar.")
                        break

                    elif confirmacion == '0':
                        print("Operación cancelada. Presione Enter para continuar.")
                    else:
                        print("Opción no válida. Operación cancelada. Presione Enter para continuar.")
                    break
                
            if not encontrado:
                limpiar_consola()
                print("  Presione '0' para volver al menú anterior\n")
                print(f"No se encontró ningún libro con ID '{id_libro}'. Presione Enter para continuar.")
                input()     
            
    # MENU DE LIBROS
    def menu (self):
        continuar = True
        while continuar:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f'''             Biblioteca
                   {Libros.REGISTRAR_LIBRO}) Agregar libros
                   {Libros.CONSULTAR_LIBRO}) Consultar Libros
                   {Libros.EDITAR_LIBRO}) Editar Libros
                   {Libros.ELIMINAR_LIBRO}) Eliminar Libros
                   {Libros.SALIR} ) Salir ''')
            opc = input ("Selecciona una Opción: ")
            try:
                opc = int (opc)
            except:
                opc = -1
            match opc:
                case Libros.REGISTRAR_LIBRO:
                    self.agregar_libros ()
                case Libros.CONSULTAR_LIBRO:
                    self.consultar_libros ()
                case Libros.ELIMINAR_LIBRO:
                    self.eliminar_libros ()
                case Libros.EDITAR_LIBRO:
                    self.editar_libros ()
                case Libros.SALIR:
                    continuar = False
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ('Opción no Válida.')

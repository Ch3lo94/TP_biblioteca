import json
from Socio import *
import os
import pathlib

# Valores de Menu de socios
class Socios:
    SALIR = 0
    REGISTRAR_SOCIO = 1
    CONSULTAR_SOCIO = 2
    EDITAR_SOCIO = 3
    ELIMINAR_SOCIO = 4


    # Constructor donde se crea coleccion de socios
    def __init__(self):
        self._socios = []
        self.ultimo_id = 0
        # Recuperar socios de ruta para que se agreguen a la lista de recuperar_socios
        self.recuperar_socios('socios.json')

    # Destructor de clase
    def __del__(self):
        self.guardar_socios ('socios.json')

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
    def socios (self):
        return self._socios
    @socios.setter
    def socios (self,valor):
        self._socios = valor
    @socios.deleter
    def socios (self):
        del self._socios

        # VALIDAR QUE NO HAYA CAMPOS VACÍOS
    def _validar_input(self, nombre_campo):
        valor = input(f"{nombre_campo}")
        while not valor.strip():  # Verifica si el valor está vacío
            print(f"El {nombre_campo.lower()} no puede estar vacío. Favor ingrese un {nombre_campo.lower()} válido.")
            valor = input(f"{nombre_campo}")
        return valor

        # RECUPERAR SOCIOS DESDE JSON
    def recuperar_socios (self, ruta):
        # Si existe la ruta
        if pathlib.Path (ruta).exists():
            # Que se abra el archivo como lectura (por eso la 'r')
            with open (ruta, 'r',encoding='utf-8') as archivo:
                datos = json.load(archivo)
            # Recuperar ultimo_id
            self._ultimo_id = datos.get('ultimo_id', 0)
            # A partir del diccionario crea el socio y lo regresa
            for socio in datos ['socios']:
                self.socios.append(traer_desde_json_Socio(socio))

    def guardar_socios (self,ruta):
        # Que se abra el archivo como escritura (por eso la 'w')
        with open (ruta, 'w',encoding='utf-8') as archivo:
            # Escribir esa informacion usando la clase creada en Socio (se usa indent para que sea mas legible a la anidacion con 4 espacios)
            json.dump({'ultimo_id': self._ultimo_id, 'socios':self.socios}, archivo, cls=socio_Encoder, indent=4)

    def imprimir_socios(self):      # Para imprimir lista de socios
            print(f"  {'ID':<5} | {'Nombre':^15} | {'Apellido':^15} | {'F/N':^10} | {'Dirección':^25} | {'Correo':^35} | {'Teléfono':^15}")
            print('-' * 140)
            for soc in self.socios:
                print(f"  {soc.id:<5} | {soc.nombre:^15} | {soc.apellido:^15} | {soc.f_nacim:^10} | {soc.direccion:^25} | {soc.correo:^35} | {soc.telefono:^15}")
            print("")

    def agregar_socios (self):
        # Limpiar consola
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('                    Agregar Socio')
        nombre = self._validar_input ("Nombre: ")
        apellido = self._validar_input ("Apellido: ")
        f_nacim = self._validar_input ("Fecha de Nacimiento (DD-MM-AAAA): ")
        direccion = self._validar_input ("Dirección: ")
        correo = self._validar_input ("Correo: ")
        tel = self._validar_input ("Teléfono: ")
       
        # Incrementar último ID y agregar los socios a la clase Socio
        self._ultimo_id += 1        
        self.socios.append (Socio(str(self._ultimo_id),nombre,apellido,f_nacim,direccion,correo,tel))
        self.guardar_socios('socios.json')


    def consultar_socios (self):
        if len(self.socios) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                    Consultar Socios')
            print("No hay Socios registrados")
            input("Presione enter para continuar.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                    Consultar Socios')
            self.imprimir_socios()
            input ("Presione Enter para continuar.")

    def eliminar_socios(self):          
        def limpiar_consola():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                     Eliminar Socio')
            print("Socios afiliados para eliminar:")
            self.imprimir_socios()

        while True:
            if len(self.socios) == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('                     Eliminar Socio')
                print("No hay Socios registrados")
                input("Presione enter para continuar.")
                break

            limpiar_consola()
            # Opciones para eliminar o volver atrás
            print("  Presione '0' para volver al menú anterior\n")
            id_socio = input("Ingrese el ID del Socio que desea eliminar: ")

            if id_socio == '0':
                print("Volviendo al menu. Presione Enter para continuar.")
                input()
                break
               
            if id_socio.strip() == '':  # Si el valor está vacío, mostrar mensaje y pedir de nuevo
                print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
                input("Presione enter para continuar.")
                limpiar_consola()
                print("  Presione '0' para volver al menú anterior\n")
                continue  # Volver a solicitar el ID

            encontrado = False

            for socio in self.socios:
                if socio.id == id_socio:
                    encontrado = True
                    limpiar_consola()
                    print(f"¿Desea eliminar el socio '{socio.nombre} {socio.apellido}'?")
                    print("     0. Cancelar")
                    print("     1. Confirmar")
                    confirmacion = input("Ingrese el número de la opción que desea realizar: ")

                    if confirmacion == '1':
                        self.socios.remove(socio)
                        self.guardar_socios('socios.json')  # Guardar cambios en el archivo JSON
                        limpiar_consola ()
                        print(f"Socio '{socio.nombre} {socio.apellido}' eliminado exitosamente. Presione Enter para continuar.")
                        input ()
                    elif confirmacion == '0':
                        print("Operación cancelada. Presione Enter para continuar.")
                    else:
                        print("Opción no válida. Operación cancelada. Presione Enter para continuar.")
                    break
            
            if not encontrado:
                limpiar_consola()
                print("  Presione '0' para volver al menú anterior\n")
                print(f"No se encontró ningún socio con ID '{id_socio}'. Presione Enter para continuar.")
                input()

    def editar_socios(self):      
        def limpiar_consola():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                     Editar Socio')
            print("Socios afiliados para editar:")
            self.imprimir_socios()

        while True:
            if len(self.socios) == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('                     Editar Socio')
                print("No hay Socios registrados")
                input("Presione enter para continuar.")
                break

            limpiar_consola()
            print("  Presione '0' para volver al menú anterior\n")
            id_socio = input("Ingrese el ID del Socio que desea editar: ")
            
            if id_socio.strip() == '':  # Si el valor está vacío, mostrar mensaje y pedir de nuevo
                print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
                input("Presione enter para continuar.")
                limpiar_consola()
                print("  Presione '0' para volver al menú anterior\n")
                continue  # Volver a solicitar el ID

            if id_socio == '0':
                print("Volviendo al menu. Presione Enter para continuar.")
                input()
                break

            encontrado = False

            for socio in self.socios:
                if socio.id == id_socio:
                    encontrado = True
                    limpiar_consola()
                    print(f"¿Desea editar el socio '{socio.nombre} {socio.apellido}'?")
                    print("     0. Cancelar")
                    print("     1. Confirmar")
                    confirmacion = input("Ingrese el número de la opción que desea realizar: ")
                    limpiar_consola()
                    
                    if confirmacion == '1':
                        nombre = input("Nombre: ")
                        apellido = input("Apellido: ")
                        f_nacim = input("Fecha de Nacimiento (DD-MM-AAAA): ")
                        direccion = input("Dirección: ")
                        correo = input("Correo: ")
                        tel = input("Teléfono: ")

                            # Actualizar los datos del socio
                        if nombre.strip():
                            socio.nombre = nombre
                        if apellido.strip():
                            socio.apellido = apellido
                        if f_nacim.strip():
                            socio.f_nacim = f_nacim
                        if direccion.strip():
                            socio.direccion = direccion
                        if correo.strip():
                            socio.correo = correo
                        if tel.strip():
                            socio.telefono = tel

                        self.guardar_socios('socios.json')  # Guardar los cambios en el archivo JSON
                        limpiar_consola ()
                        print("Socio actualizado correctamente.")
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
                print(f"No se encontró ningún socio con ID '{id_socio}'. Presione Enter para continuar.")
                input()



    # MENU DE SOCIOS
    def menu (self):
        continuar = True
        while continuar:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f'''             Biblioteca
                   {Socios.REGISTRAR_SOCIO}) Agregar Socios
                   {Socios.CONSULTAR_SOCIO}) Consultar Socios
                   {Socios.EDITAR_SOCIO}) Editar Socios
                   {Socios.ELIMINAR_SOCIO}) Eliminar Socios
                   {Socios.SALIR} ) Salir ''')
            opc = input ("Selecciona una Opción: ")
            try:
                opc = int (opc)
            except:
                opc = -1
            match opc:
                case Socios.REGISTRAR_SOCIO:
                    self.agregar_socios ()
                case Socios.CONSULTAR_SOCIO:
                    self.consultar_socios ()
                case Socios.ELIMINAR_SOCIO:
                    self.eliminar_socios ()
                case Socios.EDITAR_SOCIO:
                    self.editar_socios ()
                case Socios.SALIR:
                    continuar = False
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ('Opción no Válida.')

# Menu de Biblioteca

import os
from biblioteca_libros import Libros
from biblioteca_socios import Socios
from biblioteca_prestamos import Prestamos



class Biblioteca():
    SALIR = 0
    LIBROS = 1
    SOCIOS = 2
    PRESTAMOS = 3

    def submenu_libros (self):                      # Llama al submenu libros
        bib_libros = Libros()
        bib_libros.menu ()
    
    def submenu_socios (self):                      # Llama al submenu socios
        bib_socios = Socios()
        bib_socios.menu ()
    
    def submenu_prestamos (self):                   # Llama al submenu prestamos
        bib_libros = Libros()
        bib_socios = Socios()
        bib_prestamos = Prestamos(bib_libros,bib_socios)
        bib_prestamos.menu ()

    def menu (self):                                # Menu Biblioteca
        continuar = True
        while continuar:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f'''             Biblioteca
                   {Biblioteca.LIBROS}) Libros
                   {Biblioteca.SOCIOS}) Socios
                   {Biblioteca.PRESTAMOS}) Prestamos
                   {Biblioteca.SALIR} ) Salir ''')
            opc = input ("Selecciona una Opción: ")
            try:
                opc = int (opc)
            except:
                opc = -1
                
            match opc:    
                case Biblioteca.LIBROS:            # Llama a la opcion elegida y ejecuta la funcion
                    self.submenu_libros ()
                case Biblioteca.SOCIOS:
                    self.submenu_socios ()
                case Biblioteca.PRESTAMOS:
                    self.submenu_prestamos ()
                case Biblioteca.SALIR:
                    continuar = False
                case _:
                    os.system ('cls')
                    print ('Opción no Válida.')

            if continuar:
                input ("Presiona enter para continuar")
        input ("Presiona enter para salir")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()
# ● ID de Libro (número único y autoincremental)
# ● Título
# ● Autor
# ● Editorial
# ● Año de Publicación
# ● Género
# ● Cantidad Disponible

# Importar json
import json

# Definicion de clase y atributos a Libro
class Libro():
    def __init__(self,id,titulo,autor,editorial,anio,genero,cantidad_disp):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._editorial = editorial
        self._anio = anio
        self._genero = genero
        self._cantidad_disp = cantidad_disp

#Propiedades de cada atributo de Libro
    @property
    def id (self):
        return self._id
    @id.setter
    def id(self, valor):
        self._id = valor
    @id.deleter
    def id(self):
        del self._id

    @property
    def titulo (self):
        return self._titulo
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
    @titulo.deleter
    def titulo(self):
        del self._titulo

    @property
    def autor (self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        self._autor = valor
    @autor.deleter
    def autor(self):
        del self._autor

    @property
    def editorial (self):
        return self._editorial
    @editorial.setter
    def editorial(self, valor):
        self._editorial = valor
    @editorial.deleter
    def editorial(self):
        del self._editorial

    @property
    def anio (self):
        return self._anio
    @anio.setter
    def anio(self, valor):
        self._anio = valor
    @anio.deleter
    def anio(self):
        del self._anio

    @property
    def genero (self):
        return self._genero
    @genero.setter
    def genero(self, valor):
        self._genero = valor
    @genero.deleter
    def genero(self):
        del self._genero

    @property
    def cantidad_disp (self):
        return self._cantidad_disp
    @cantidad_disp.setter
    def cantidad_disp(self, valor):
        self._cantidad_disp = valor
    @cantidad_disp.deleter
    def cantidad_disp(self):
        del self._cantidad_disp

# Metodo String para imprimir
    def __str__ (self):
        Esp = 25
        return f'''{"ID: " : <{Esp}}{self.id}
{"Título: " : <{Esp}}{self.titulo}
{"Autor: " : <{Esp}}{self.autor}
{"Editorial: " : <{Esp}}{self.editorial}
{"Año: " : <{Esp}}{self.anio}
{"Género: " : <{Esp}}{self.genero}
{"Cantidad Disponible: " : <{Esp}}{self.cantidad_disp}'''

# Convertir objeto a formato JSON
class libro_Encoder (json.JSONEncoder):
    def default (self, obj):
        if isinstance(obj, Libro):
            return {'id':obj.id,'titulo':obj._titulo,'autor':obj.autor,'editorial':obj.editorial,'anio':obj.anio,'genero':obj.genero,'cantidad_disp':obj.cantidad_disp}
        return json.JSONEncoder.default(self,obj)

# Convertir JSON a Objeto   
def traer_desde_json_Libro (diccionario):
    return Libro (diccionario ['id'], diccionario ['titulo'], diccionario ['autor'], diccionario ['editorial'], diccionario ['anio'], diccionario ['genero'], diccionario ['cantidad_disp'])


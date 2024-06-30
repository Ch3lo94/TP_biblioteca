# Importar json
import json

# Definicion de clase y atributos a Socio
class Socio():
    def __init__(self,id_socio,nombre,apellido,f_nacim,direccion,correo,tel):
        self._socio = id_socio
        self._nombre = nombre
        self._apellido = apellido
        self._f_nacim = f_nacim
        self._direccion = direccion
        self._correo = correo
        self._tel = tel

#Propiedades de cada atributo de Socio
    @property
    def id (self):
        return self._socio
    @id.setter
    def id(self, valor):
        self._socio = valor
    @id.deleter
    def id(self):
        del self._socio

    @property
    def nombre (self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def apellido (self):
        return self._apellido
    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor
    @apellido.deleter
    def apellido(self):
        del self._apellido

    @property
    def f_nacim (self):
        return self._f_nacim
    @f_nacim.setter
    def f_nacim(self, valor):
        self._f_nacim = valor
    @f_nacim.deleter
    def f_nacim(self):
        del self._f_nacim

    @property
    def direccion (self):
        return self._direccion
    @direccion.setter
    def direccion(self, valor):
        self._direccion = valor
    @direccion.deleter
    def direccion(self):
        del self._direccion

    @property
    def correo (self):
        return self._correo
    @correo.setter
    def correo(self, valor):
        self._correo = valor
    @correo.deleter
    def correo(self):
        del self._correo

    @property
    def telefono (self):
        return self._tel
    @telefono.setter
    def telefono(self, valor):
        self._tel = valor
    @telefono.deleter
    def telefono(self):
        del self._tel

# Metodo String para imprimir
    def __str__ (self):
        Esp = 25
        return f'''{"ID: " : <{Esp}}{self.id}
{"Nombre: " : <{Esp}}{self.nombre}
{"Apellido: " : <{Esp}}{self.apellido}
{"Fecha de Nacimiento: " : <{Esp}}{self.f_nacim}
{"Dirección: " : <{Esp}}{self.direccion}
{"Correo electrónico: " : <{Esp}}{self.correo}
{"Teléfono: " : <{Esp}}{self.telefono}'''

# Convertir objeto a formato JSON
class socio_Encoder (json.JSONEncoder):
    def default (self, obj):
        if isinstance(obj, Socio):
            return {'id':obj.id,'nombre':obj._nombre,'apellido':obj.apellido,'f_nacim':obj.f_nacim,'direccion':obj.direccion,'correo':obj.correo,'telefono':obj.telefono}
        return json.JSONEncoder.default(self,obj)

# Convertir JSON a Objeto   
def traer_desde_json_Socio (diccionario):
    return Socio (diccionario ['id'], diccionario ['nombre'], diccionario ['apellido'], diccionario ['f_nacim'], diccionario ['direccion'], diccionario ['correo'], diccionario ['telefono'])

